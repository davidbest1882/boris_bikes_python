import unittest
import sys
sys.path.append('..')
from app import DockingStation, Bike

class TestDockingStation(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()
        self.bike = Bike()

    def test_docking_station_object(self):
        self.assertIsInstance(self.docking_station, DockingStation)

    def test_for_docked_bike(self):
        self.docking_station.dock_bike(self.bike)
        self.assertEqual(self.docking_station.docked, self.bike)
        self.docking_station.release_bike()
        with self.assertRaises(AttributeError):
            self.docking_station.release_bike()

    def test_raises_exception_if_no_bike(self):
        with self.assertRaises(AttributeError):
            self.docking_station.see_bike()


class TestBike(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()
        self.bike = Bike()

    def test_bike_object(self):
        self.assertIsInstance(self.bike, Bike)

    def test_bike_is_working(self):
        self.assertEqual(self.bike.is_working(), True)


if __name__ == '__main__':
    unittest.main()
