class DockingStation:

    def __init__(self):
        self.docked = None

    def release_bike(self):
        return Bike()

    def dock_bike(self, bike):
        self.docked = bike

    def see_bike(self):
        return self.docked

class Bike:

    def is_working(self):
        return True
