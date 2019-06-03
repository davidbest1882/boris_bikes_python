class DockingStation:

    def __init__(self):
        pass

    def release_bike(self):
        try:
             return self.docked
        except AttributeError:
            raise Exception("No bike available")
        finally:
            if hasattr(self, 'docked'):
                delattr(self, 'docked')

    def dock(self, bike):
        if hasattr(self, 'docked'):
            raise Exception("Bike already docked at this station!")
        else:
            self.docked = bike

    def show_bike(self):
        try:
            return self.docked
        except AttributeError:
            raise Exception("No bike available")

class Bike:

    def is_working(self):
        return True
