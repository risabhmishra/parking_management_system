import unittest
from parking_management import ParkingManagement


class TestParkingLot(unittest.TestCase):
    """
    This is a Test class which contains the methods for unit testing the methods present in Parking Management Class.
    All the methods have test as prefix to the method names present in the Parking Management Class and it asserts the
    value returned by the calling the method in Parking Management Class against the expected output.
    """

    def test_create_parking_lot(self):
        parking_management = ParkingManagement()
        result = parking_management.create_parking_slots(6)
        self.assertEqual(True, result)

    def test_issue_parking_ticket(self):
        parking_management = ParkingManagement()
        parking_management.create_parking_slots(6)
        result = parking_management.issue_parking_ticket("WB-01-RM-1234", "23")
        self.assertNotEqual(-1, result)

    def test_return_parking_ticket(self):
        parking_management = ParkingManagement()
        parking_management.create_parking_slots(6)
        parking_management.issue_parking_ticket("WB-01-RM-1234", "23")
        result = parking_management.return_parking_ticket(1)
        self.assertNotEqual(False, result)

    def test_get_parking_slot_number_from_vehicle_registration_number(self):
        parking_management = ParkingManagement()
        parking_management.create_parking_slots(6)
        parking_management.issue_parking_ticket("WB-01-RM-1234", "23")
        result = parking_management.get_parking_slot_number_from_vehicle_registration_number("WB-01-RM-1234")
        self.assertEqual(1, result)

    def test_get_vehicle_registration_numbers_from_driver_age(self):
        parking_management = ParkingManagement()
        parking_management.create_parking_slots(6)
        parking_management.issue_parking_ticket("WB-01-RM-1234", "23")
        result = parking_management.get_vehicle_registration_numbers_from_driver_age(23)
        self.assertEqual(["WB-01-RM-1234"], result)

    def test_get_parking_slots_from_driver_age(self):
        parking_management = ParkingManagement()
        parking_management.create_parking_slots(6)
        parking_management.issue_parking_ticket("WB-01-RM-1234", "23")
        result = parking_management.get_parking_slots_from_driver_age(23)
        self.assertEqual([1], result)


if __name__ == '__main__':
    unittest.main()
