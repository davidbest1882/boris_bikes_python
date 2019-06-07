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
        self.assertEqual(self.docking_station.bike_store, [self.bike1])
        self.docking_station.release_bike()
        with self.assertRaises(Exception):
            self.docking_station.release_bike()

    def test_show_bikes_shows_a_bike(self):
        self.docking_station.dock(self.bike1)
        self.assertEqual(self.docking_station.show_bikes(), [self.bike1])

    def test_show_bikes_raises_exception_if_no_bike(self):
        with self.assertRaises(Exception):
            self.docking_station.show_bikes()

    def test_docking_station_releases_bike(self):
        self.docking_station.dock(self.bike1)
        self.assertEqual(self.docking_station.release_bike(), self.bike1)

    def test_store_maximum_20_bikes(self):
        for i in range(20):
            self.docking_station.dock(Bike())
        self.assertEqual(len(self.docking_station.bike_store), 20)
        with self.assertRaises(Exception):
            self.docking_station.dock(Bike())



class TestBike(unittest.TestCase):

    def setUp(self):
        self.bike = Bike()

    def test_bike_object(self):
        self.assertIsInstance(self.bike, Bike)

    def test_bike_is_working(self):
        self.assertEqual(self.bike.is_working(), True)


if __name__ == '__main__':
    unittest.main()
