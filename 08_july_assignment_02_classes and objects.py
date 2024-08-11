"""
Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""
class Vehicle:

    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

    def show(self):
        print("The vehicle's speed is" , self.max_speed, 'and mileage is', self.mileage ,'km')

vehicle=Vehicle(100,50)
vehicle.show()


"""
Exercise 2: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Given:
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
Expected Output:
Vehicle Name: School Volvo Speed: 180 Mileage: 12
"""
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):

    def show(self):
        print("Vehicle name:" ,self.name,"Vehicle speed:", self.max_speed,"Vehicle mileage:", self.mileage)

bus=Bus("School Volvo",180,12)
bus.show()

"""
Exercise 3: Class Inheritance
Given:
Create a Bus class that inherits from the Vehicle class. 
Give the capacity argument of Bus.seating_capacity() a default value of 50.
Use the following code for your parent Vehicle class.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
Expected Output:
The seating capacity of a bus is 50 passengers
"""

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):

    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity)

bus=Bus("School bus",60,45)
print(bus.seating_capacity())
Bus.seating_capacity(50)