from Models.Driver import Driver
from Models.Vehicle import Vehicle


class Car(Vehicle):
    """
    Class Car inherits from the class Vehicle,
    It contains a get method for returning type of the vehicle,i.e. car and
    and a get method for returning age of the driver driving the car.
    """

    def __init__(self, registration_number, driver_age):
        """
        The constructor method initiates the constructor method for Vehicle Class,
        passing the vehicle registration number as argument.
        A new driver object is created from Driver Class, by passing driver's age as argument,
        and the object is assigned to driver attribute of the class.

        :param registration_number:string Vehicle Registration Number of the Car
        :param driver_age:int Age of the driver driving the Car
        """

        Vehicle.__init__(self, registration_number)
        self.driver = Driver(driver_age)

    def get_vehicle_type(self):
        """
        This method returns the type of vehicle, in this case 'Car' is returned.
        :return: type_of_vehicle:string
        """

        return "Car"

    def get_driver_age(self):
        """
        This method returns the age of the driver driving the car.
        :return: driver_age:int
        """

        return self.driver.get_age()
