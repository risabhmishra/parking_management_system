class ParkingTicket:
    """
    ParkingTicket class contains information about car, driver and the parking_slot in which the car is parked.
    It contains a constructor method to set the car object and parking slot in car and parking_slot parameters.
    It also contains get methods to return the vehicle registration number of the car, driver's age and
    parking slot number in which the car is parked.
    """

    def __init__(self, car, parking_slot):
        """
        This constructor method is used to assign the object of the Class Car to car attribute and parking slot number
        to parking_slot attribute of the class.
        :param car:obj
        :param parking_slot:int
        """

        self.car = car
        self.parking_slot = parking_slot

    def get_vehicle_registration_number(self):
        """
        This method is used to return the vehicle registration number of the car.
        :return: vehicle_registration_number:str
        """

        return self.car.get_registration_number()

    def get_driver_age(self):
        """
        This method is used to return the age of the driver, driving the car.
        :return: driver_age:int
        """

        return self.car.get_driver_age()

    def get_parking_slot(self):
        """
        This method is used to return the parking slot number in which the car is parked.
        :return: parking_slot:int
        """

        return self.parking_slot

    def __repr__(self):
        """
        This method is to ParkingTicket Class objects in the format,
        <Vehicle Registration Number> - <Driver's Age> - <Parking Slot Number>
        :return: object_representation:str
        """

        return f'{self.get_vehicle_registration_number()} - {self.get_driver_age()} - {self.get_parking_slot()}'
