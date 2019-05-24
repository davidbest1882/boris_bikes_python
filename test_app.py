import unittest
from app import DockingStation, Bike

class TestDockingStation(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()

    def test_docking_station_object(self):
        self.assertIsInstance(self.docking_station, DockingStation)

    def test_dock_bike(self):
        bike = self.docking_station.release_bike()
        self.assertEquals(self.docking_station.docked, None)
        self.docking_station.dock_bike(bike)
        self.assertEquals(self.docking_station.docked, bike)


class TestBike(unittest.TestCase):

    def setUp(self):
        self.docking_station = DockingStation()
        self.bike = self.docking_station.release_bike()

    def test_release_bike_creates_bike_object(self):
        self.assertIsInstance(self.bike, Bike)

    def test_bike_is_working(self):
        self.assertEquals(self.bike.is_working(), True)


if __name__ == '__main__':
    unittest.main()
