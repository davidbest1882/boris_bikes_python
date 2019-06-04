class DockingStation:

    def __init__(self):
        self.bike_store = []
        self.maximum_bikes = 20

    def release_bike(self):
        try:
             return self.docked
        except AttributeError:
            raise Exception("No bike available")
        finally:
            if hasattr(self, 'docked'):
                delattr(self, 'docked')

    def dock(self, bike):
        if len(self.bike_store) <= self.maximum_bikes:
            self.bike_store.append(bike)
        else:
            raise Exception("This station is full!")

    def show_bikes(self):
        try:
            return self.bike_store
        except AttributeError:
            raise Exception("No bike available")

class Bike:

    def is_working(self):
        return True
