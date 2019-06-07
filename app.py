class DockingStation:

    def __init__(self):
        self.bike_store = []
        self.capacity = 20
        self.minumum_bikes = 1

    def release_bike(self):
        try:
            return self.bike_store.pop()
        except Exception:
            raise Exception("No bike available")

    def dock(self, bike):
        try:
            self.__is_full()
        except Exception as e:
            raise e
        else:
            self.bike_store.append(bike)

    def show_bikes(self):
        if len(self.bike_store) >= self.minumum_bikes:
            return self.bike_store
        else:
            raise Exception('No bikes available')

    def __is_full(self):
        if len(self.bike_store) >= self.capacity:
            raise Exception("This station is full!")


class Bike:

    def is_working(self):
        return True
