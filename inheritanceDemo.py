class vehicle:

    def vehicle_info(self):
        print("inside vehicle class")

class car(vehicle):

    def car_info(self):
        print("Inside car class which ahs inherited main class vehicle")

c1=car()
c1.car_info()
c1.vehicle_info()