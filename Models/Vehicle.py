class Vehicle:
    """
    Vehicle Class acts as a parent base class for all types of vehicles, for instance in our case it is Car Class.
    It contains a constructor method to set the registration number of the vehicle to registration_number attribute
    of the class and a get method to return the value stored in registration_number attribute of the class.
    """

    def __init__(self, registration_number):
        """
        This constructor method is used to store the registration number of the vehicle to registration_number attribute
        of the class.
        :param registration_number: str
        """

        self.registration_number = registration_number

    def get_registration_number(self):
        """
        This method is used to return the value stored in the registration_number attribute of the class.
        :return: registration_number:str
        """

        return self.registration_number
