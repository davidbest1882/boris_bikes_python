import unittest
from app import DockingStation

class TestDockingStation(unittest.TestCase):

    def setUp(self):
        pass

    def test_docking_station_object(self):
        docking_station = DockingStation()
        self.assertIsInstance(docking_station, DockingStation)

    def test_release_bike_returns_true(self):
        docking_station = DockingStation()
        self.assertEqual(docking_station.release_bike(), True)

if __name__ == '__main__':
    unittest.main()
