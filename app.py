class DockingStation:

    def __init__(self):
        self.docked = False

    def release_bike(self):
        if self.docked == False:
            raise Exception("No bike available")
        else:
            return self.docked

    def dock_bike(self, bike):
        self.docked = bike

    def see_bike(self):
        return self.docked

class Bike:

    def is_working(self):
        return True
