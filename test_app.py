import unittest
from app import DockingStation, Bike

class TestDockingStation(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()

    def test_docking_station_object(self):
        self.assertIsInstance(self.docking_station, DockingStation)

    def test_for_docked_bike(self):
        bike = Bike()
        self.docking_station.dock_bike(bike)
        self.assertTrue(self.docking_station.docked)

    def test_raises_exception_if_no_bike(self):
        with self.assertRaises(Exception):
            self.docking_station.release_bike()


class TestBike(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()
        self.bike = Bike()

    def test_bike_object(self):
        self.assertIsInstance(self.bike, Bike)

    def test_bike_is_working(self):
        self.assertEquals(self.bike.is_working(), True)


if __name__ == '__main__':
    unittest.main()
