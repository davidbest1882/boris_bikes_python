class DockingStation:

    def __init__(self):
        pass

    def release_bike(self):
        try:
             return self.docked
        except AttributeError as e:
            raise e
        finally:
            if hasattr(self, 'docked'):
                delattr(self, 'docked')

        # if self.docked == False:
        #     raise Exception("No bike available")
        # else:
        #     return self.docked
        #     self.docked = False

    def dock_bike(self, bike):
        self.docked = bike

    def see_bike(self):
        try:
            return self.docked
        except AttributeError as e:
            raise e

class Bike:

    def is_working(self):
        return True
