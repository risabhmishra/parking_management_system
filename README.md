## Parking Management System

An Automated Parking Ticketing based Parking Management System using Python.

## Dependencies

You just need Python. The code is compatible with Python3. Visit the link https://www.python.org/downloads/ to install Python. 

## Description

This repository gives an overview of designing an Automated Parking Ticketing based Parking Management System using Python.
The Parking Management System can create n number of parking slots in a parking lot. It will issue a parking ticket on entrance terminal
and receive back the parking ticket on the exit terminal. The parking ticket will contain vehicle registration number of car,
age of the driver driving the car and parking slot allocated to the car. The parking slot allocated to a car will always be the nearest 
to the entrance terminal. On returning the parking ticket the parking slot will be vacated and deallocated from the car.
The Parking Management System can execute a set of predefined commands mentioned below to perform some operations on the Parking Lot.



Following assumptions have been made while designing the Parking Management System :-

1. There will be maximum 1000 number of parking slots in a parking lot.
2. There will be only 1 entrance and 1 exit in a parking lot.
3. Parking slot numbers will always be in the range 1-1000, Increasing based on distance from the entry point in steps of one.
4. Customers collect parking ticket at entrance and parking slot is assigned on the ticket.
5. Parking slot assigned will be nearest to the entrance.
6. The Parking Ticket issued will contain - Vehicle Registration Number, Age of Driver and Parking Slot Assigned.
7. Parking Management System should not allow more vehicles to enter than the number of parking slots.
8. On Exit - Return the Parking Ticket and mark the parking slot used by vehicle as vacant

Class ParkingManagement defines the following methods :-
1. `create_parking_slots(self, max_capacity)` - Given max_capacity, Create max_capacity number of parking slots in a parking lot.
2. `get_nearest_empty_parking_slot(self)` - Get a vacant parking slot nearest to the entrance.
3. `allocate_parking_slot(self, car)` - Given an object of Class Car, Allocate a parking slot to the car.
4. `deallocate_parking_slot(self, parking_slot_number)` - Given a parking slot number, Deallocate it from the car it was allocated to.
5. `issue_parking_ticket(self, vehicle_registration_number, driver_age)` - Given Vehicle Registration Number and Driver's age,
Issue a parking ticket to the vehicle on entry terminal.
6. `return_parking_ticket(self, parking_slot_number)` - Given Parking Slot Number, Accept back the parking ticket issued to a vehicle on exit terminal.
7. `get_parking_slot_number_from_vehicle_registration_number(self, vehicle_registration_number)` - Given Vehicle Registration Number,
Find the Parking Slot number it is parked in.
8. `get_vehicle_registration_numbers_from_driver_age(self, driver_age)` - Given a driver_age, Get a list of vehicle registration numbers, 
whose driver's age matches with the driver_age parameter.
9. `get_parking_slots_from_driver_age(self, driver_age)` - Given a driver_age, Get a list of parking slot numbers, 
where the age of the driver of the car parked in that parking slot matches with the driver_age parameter.
10. `parse_commands(self, query)` - Given an Input Query, Parse the command and arguments and execute the query.



Predefined Commands that the Parking Management System can execute in the form of queries specified in `<input_file>`:
1. `Create_parking_lot <max_capacity:int>`
2. `Park <vehicle_registration_number:str> driver_age <driver_age:int>`
3. `Leave <parking_slot:int>`
4. `Slot_number_for_car_with_number <vehicle_registration_number:str>`
5. `Slot_numbers_for_driver_of_age <driver_age:int>`
6. `Vehicle_registration_number_for_driver_of_age <driver_age:int>`


Model Classes used in this project are present inside `Models` directory. These include :-
1. Class `Vehicle` - Vehicle Class acts as a parent base class for all types of vehicles, for instance in our case it is Car Class.
2. Class `Car` - Class Car inherits from the Class Vehicle,and it contains information about the vehicle and the driver driving it.
3. Class `Driver` - Class Driver contains all information about the driver.
4. Class `ParkingTicket` - ParkingTicket class contains information about car, driver and the parking_slot in which the car is parked.



Python program parking_management.py takes in a `<input_file>` as a mandatory input and a `<output_file>` as an optional input.
It can print output to terminal console or write to an output file based on the optional input `<output_file>`.
An example input_file `sample_input.txt` has been provided inside `Data` directory.


I have followed TDD approach while designing this. `test_parking_management.py` uses `unittest` module of python.
Here 6 test cases are written in order to test each functionality mentioned in parking_management.py

## Setup

To Setup and Run Parking Management System - 

1. Clone the repository

2. Run `python3 parking_management.py --input_file=<input_file_path>` to run without output_file. 
This will print all the output to terminal console.

![image](https://user-images.githubusercontent.com/21499789/128347936-029489c4-3218-4dcc-bd61-980005f26369.png)
  
3. Run `python3 parking_management.py --input_file=<input_file_path> --output_file=<output_file_path>` to run with output_file. 
This will write all the output to the output_file.

4. You can also run the test cases separately as `python3 test_parking_management.py`. 
This runs the 6 test cases written in file. 

![image](https://user-images.githubusercontent.com/21499789/128348027-4d99b58c-88ca-459d-8b6d-ead1f41d2319.png)
