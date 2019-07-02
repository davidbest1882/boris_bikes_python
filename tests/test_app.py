from unittest.mock import MagicMock as Mock

import unittest
import sys
sys.path.append('..')
from app import DockingStation, Bike

class TestDockingStation(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()
        self.bike1 = Mock()
        self.bike1.configure_mock(working=True)
        self.bike2 = Mock()

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

    def test_default_bike_capacity(self):
        for i in range(20):
            self.docking_station.dock(Bike())
        self.assertEqual(len(self.docking_station.bike_store), 20)
        with self.assertRaises(Exception):
            self.docking_station.dock(Bike())

    def test_lower_and_higher_bike_capacity(self):
        for default in [10, 30]:
            self.docking_station = DockingStation(default)
            for bike in range(default):
                self.docking_station.dock(Bike())
            self.assertEqual(len(self.docking_station.bike_store), default)
            with self.assertRaises(Exception):
                self.docking_station.dock(Bike())

    def test_release_bike_thats_working(self):
        self.bike1.report_broken()
        self.docking_station.dock(self.bike1)
        self.docking_station.dock(self.bike2)
        self.bike3 = self.docking_station.release_bike()
        self.assertEqual(self.bike3.working, True)


class TestBike(unittest.TestCase):

    def setUp(self):
        self.bike = Bike()

    def test_bike_object(self):
        self.assertIsInstance(self.bike, Bike)

    def test_bike_is_working(self):
        self.assertEqual(self.bike.working, True)

    def test_report_broken(self):
        self.bike.report_broken()
        self.assertEqual(self.bike.working, False)


if __name__ == '__main__':
    unittest.main()
