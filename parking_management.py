import argparse
import sys
from heapq import heapify, heappush, heappop

from Models.Car import Car
from Models.ParkingTicket import ParkingTicket


class ParkingManagement:
    """
    This is the Main Class for Managing Automated Parking Ticketing System.
    """

    def __init__(self):
        """
        This constructor method is used to initialize the capacity, available_parking_slots and occupied_parking_slots
        parameters of the class.
        capacity -> It is initialized to zero.
        available_parking_slots -> It is initialized to an empty list.
        occupied_parking_slots -> It is initialized to an empty dictionary.
        """

        self.capacity = 0
        self.available_parking_slots = []
        self.occupied_parking_slots = {}

    def create_parking_slots(self, max_capacity):
        """
        This method takes in the max capacity of the parking lot and returns a min heap for all available parking lots.
        :param max_capacity:int It denotes the maximum capacity of the parking lot.
        :return: status:boolean It returns True if a min heap containing parking lots in the range [1..capacity],
        is successfully created otherwise it return False if an exception is thrown in the process.
        """

        try:
            self.capacity = max_capacity

            # Creating empty available_parking_lots heap
            heapify(self.available_parking_slots)

            # Adding parking_lots_index in the range [1..capacity] to the available_parking_lots_heap using heappush
            # function.
            for parking_slots_index in range(1, self.capacity + 1):
                heappush(self.available_parking_slots, parking_slots_index)

            return True
        except Exception as exception:
            print(exception)
            return False

    def get_nearest_empty_parking_slot(self):
        """
        This method returns the minimum value from the available_parking_slots min heap.
        :return: available_parking_slot:int The nearest available parking slot to the entry terminal.
        """

        available_parking_slot = heappop(self.available_parking_slots)
        return available_parking_slot

    def allocate_parking_slot(self, car):
        """
        This method is used to allocate the nearest available parking slot to the car entering the entry terminal.
        :param car:obj Object of the Car Class, to which the parking slot has to be allocated.
        :return: parking_slot:int It returns the assigned parking_slot to car or -1 if no parking_slot is available.
        """

        # Checking if there are vacant slots available in the parking lot
        if len(self.occupied_parking_slots) < self.capacity:
            parking_slot = self.get_nearest_empty_parking_slot()
            vehicle_registration_number = car.get_registration_number()

            # A parking ticket is created for the car with vehicle registration number, driver's age and parking slot
            # assigned mentioned on the ticket.
            parking_ticket = ParkingTicket(car, parking_slot)

            # Set the parking_ticket as value to key vehicle_registration_number in the occupied_parking_slots
            # dictionary.
            self.occupied_parking_slots[vehicle_registration_number] = parking_ticket
        else:
            parking_slot = -1

        return parking_slot

    def deallocate_parking_slot(self, parking_slot_number):
        """
        This method is used to deallocate the parking slot number assigned to a car when it's vacating the parking slot,
        and leaving from the exit terminal.
        :param parking_slot_number:int Parking Slot Number which is getting vacated.
        :return: parking_ticket:obj or False:boolean based on the deallocate status of the parking slot.
        """

        if len(self.occupied_parking_slots) > 0:
            key = -1

            # Looking up the vehicle_registration_number and parking_ticket for the car which is allocated
            # the parking_slot_number passed as argument, in occupied_parking_slots dictionary.
            for vehicle_registration_number, parking_ticket in self.occupied_parking_slots.items():
                if parking_ticket.get_parking_slot() == parking_slot_number:
                    key = vehicle_registration_number
                    value = parking_ticket
                    break
            if key == -1:
                # If no car found which is allocated the parking_slot_number passed as argument, return False.
                return False
            else:
                # Deleting the entry for the car vacating the parking_slot and pushing the vacated parking slot number
                # back to available_parking_slots min heap.
                del self.occupied_parking_slots[key]
                heappush(self.available_parking_slots, parking_slot_number)
                return value
        else:
            return False

    def issue_parking_ticket(self, vehicle_registration_number, driver_age):
        """
        This method is used to issue parking ticket to the car entering the parking lot from the entry terminal.
        :param vehicle_registration_number:str Vehicle registration Number of the car
        :param driver_age:int Age of the driver driving the car
        :return: parking_slot:int It returns the parking slot number allocated to the car
        """

        # Create an object of Class Car by passing vehicle_registration_number and driver_age as arguments.
        car = Car(vehicle_registration_number, driver_age)

        parking_slot = self.allocate_parking_slot(car)

        return parking_slot

    def return_parking_ticket(self, parking_slot_number):
        """
        This method is used to deallocate the parking slot number allocated to a car on returning parking ticket,
        while vacating the parking slot and exiting parking lot from the exit terminal.
        :param parking_slot_number:int Parking Slot number that was allocated to the car.
        :return: parking_slot_number:int Vacated parking slot number
        """

        return self.deallocate_parking_slot(parking_slot_number)

    def get_parking_slot_number_from_vehicle_registration_number(self, vehicle_registration_number):
        """
        This method is used to look up the occupied_parking_slots dictionary and return the assigned parking_slot number
        from the parking ticket for the vehicle_registration_number passed as argument.
        :param vehicle_registration_number:str Vehicle Registration Number of the Car whose allocated parking_slot is to
        be looked upon and returned
        :return: parking_slot:int Parking Slot number occupied by the car with the vehicle_registration_number passes
        as argument.
        """

        parking_slot = -1

        if vehicle_registration_number in self.occupied_parking_slots:
            parking_slot = self.occupied_parking_slots[vehicle_registration_number].get_parking_slot()

        return parking_slot

    def get_vehicle_registration_numbers_from_driver_age(self, driver_age):
        """
        This method is used to look up the occupied_parking_slots dictionary and return the vehicle registration numbers
        for the cars whose driver's age matches with the driver_age passed as argument in the parking ticket.
        :param driver_age:int Age of the driver
        :return: vehicle_registration_numbers:list List of all vehicle_registration_numbers for which driver's age
        matches with the driver_age passed as argument in the parking ticket.
        """

        vehicle_registration_numbers = []

        for vehicle_registration_number, parking_ticket in self.occupied_parking_slots.items():
            if parking_ticket.get_driver_age() == driver_age:
                vehicle_registration_numbers.append(vehicle_registration_number)

        return vehicle_registration_numbers

    def get_parking_slots_from_driver_age(self, driver_age):
        """
        This method is used to look up the occupied_parking_slots dictionary and return the allocated parking_slots
        for the cars whose driver's age matches with the driver_age passed as argument in the parking ticket.
        :param driver_age:int Age of the driver
        :return: parking_slots:list List of parking_slots allocated to the cars for which driver's age
        matches with the driver_age passed as argument in the parking ticket.
        """

        parking_slots = []

        for parking_ticket in self.occupied_parking_slots.values():
            if parking_ticket.get_driver_age() == driver_age:
                parking_slots.append(parking_ticket.get_parking_slot())

        return parking_slots

    def parse_commands(self, query):
        """
        This method takes query as input and executes the query on the predefined set of commands and matching methods
        to be executed, and prints the output to the console or writes it to a output file based on the mode selected.

        Predefined Commands :
        1. Create_parking_lot <capacity:int>
        2. Park <vehicle_registration_number:str> driver_age <age:int>
        3. Leave <parking_slot:int>
        4. Slot_number_for_car_with_number <vehicle_registration_number:str>
        5. Slot_numbers_for_driver_of_age <age:int>
        6. Vehicle_registration_number_for_driver_of_age <age:int>

        :param query:str Command to be executed with arguments separated by " ".
        """

        if query.startswith('Create_parking_lot'):
            try:
                capacity = int(query.split(' ')[1])
                status = self.create_parking_slots(capacity)
                if status:
                    print(f'Created parking of {capacity} slots')

            except Exception as exception:
                print(f'Error in Query - {query} : {exception}')

        elif query.startswith('Park'):
            try:
                vehicle_registration_number = query.split(' ')[1]
                driver_age = query.split(' ')[3]
                result = self.issue_parking_ticket(vehicle_registration_number, driver_age)
                if result == -1:
                    print('Sorry, Parking Lot is full, No Parking Slots Available.')
                else:
                    print(
                        f'Car with vehicle registration number "{vehicle_registration_number}" has been parked at '
                        f'slot number {result}')
            except Exception as exception:
                print(f'Error in Query - {query} : {exception}')

        elif query.startswith('Leave'):
            try:
                leaving_parking_slot = int(query.split(' ')[1])
                parking_ticket = self.return_parking_ticket(leaving_parking_slot)
                if parking_ticket:
                    print(f'Slot number {parking_ticket.get_parking_slot()} vacated, the car with vehicle registration '
                          f'number "{parking_ticket.get_vehicle_registration_number()}" left the space, the driver of '
                          f'the car was of age {parking_ticket.get_driver_age()}')
                else:
                    print(f'Slot number {leaving_parking_slot} cannot be vacated.')
            except Exception as exception:
                print(f'Error in Query - {query} : {exception}')

        elif query.startswith('Slot_number_for_car_with_number'):
            try:
                car_registration_number = query.split(' ')[1]

                parking_slot = self.get_parking_slot_number_from_vehicle_registration_number(car_registration_number)

                if parking_slot == -1:
                    print('No parked car matches the query')
                else:
                    print(parking_slot)
            except Exception as exception:
                print(f'Error in Query - {query} : {exception}')

        elif query.startswith('Vehicle_registration_number_for_driver_of_age'):
            try:
                driver_age = int(query.split(' ')[1])

                vehicle_registration_numbers = self.get_vehicle_registration_numbers_from_driver_age(driver_age)

                if len(vehicle_registration_numbers) > 0:
                    print(','.join(vehicle_registration_numbers))
                else:
                    print('No parked car matches the query')
            except Exception as exception:
                print(f'Error in Query - {query} : {exception}')

        elif query.startswith('Slot_numbers_for_driver_of_age'):
            try:
                driver_age = int(query.split(' ')[1])

                parking_slots = self.get_parking_slots_from_driver_age(driver_age)
                if len(parking_slots) > 0:
                    print(','.join([str(parking_slot) for parking_slot in parking_slots]))
                else:
                    print('No parked car matches the query')
            except Exception as exception:
                print(f'Error in Query - {query} : {exception}')

        else:
            print('Query not recognized.')


if __name__ == '__main__':
    # Creates an object of Main Class Parking Management
    parking_management = ParkingManagement()

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', action="store", required=True, dest='input_file', help="Input File")
    parser.add_argument('--output_file', action="store", required=False, dest='output_file', help="Output File")

    args = parser.parse_args()

    # if output_file is argument is specified, all the console output will be written to the output_file.
    if args.output_file:
        sys.stdout = open(args.output_file, "w")

    # Iterating through the input_file line by line and passing it to parse_commands method of Parking Management Class.
    if args.input_file:
        with open(args.input_file) as input_file:
            for line in input_file:
                line = line.rstrip('\n')
                parking_management.parse_commands(line)
