class Driver:
    """
    Class Driver contains all information about the driver.
    It contains a constructor method to set the age attribute of the driver,
    and a get method to return the age attribute of the driver.
    """

    def __init__(self, age):
        """
        This constructor method sets the age driver's age to the age attribute of the driver class.
        :param age:int driver's age
        """

        self.age = int(age)

    def get_age(self):
        """
        This get_age method is used to return the age attribute of the driver class.
        :return: age:int driver's age
        """

        return self.age
