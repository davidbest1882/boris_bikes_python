import unittest
import sys
sys.path.append('..')
from app import DockingStation, Bike

class TestDockingStation(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()
        self.bike1 = Bike()
        self.bike2 = Bike()

    def test_docking_station_object(self):
        self.assertIsInstance(self.docking_station, DockingStation)

    def test_for_docked_bike(self):
        self.docking_station.dock(self.bike1)
        self.assertEqual(self.docking_station.docked, self.bike1)
        self.docking_station.release_bike()
        with self.assertRaises(Exception):
            self.docking_station.release_bike()

    def test_raises_exception_if_no_bike(self):
        with self.assertRaises(Exception):
            self.docking_station.show_bike()

    def test_bike_already_docked(self):
        self.docking_station.dock(self.bike1)
        with self.assertRaises(Exception):
            self.docking_station.dock(self.bike2)



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
