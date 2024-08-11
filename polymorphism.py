
#used with inheritance
#existing class using method overriding.
#has same name as methods in parent class
#process of reimplementing inherited method in child class is called method overriding
"""
students=['ashwini','bala','karthick']
school="natwest school"

#calculate count

print(len(students)) #prints length of list
print(len(school)) #prints length of chars

"""

class Vehicle:

    def __init__(self,name, color,price):
        self.name=name
        self.color=color
        self.price=price

    def max_speed(self):
        print("max speed is 150 in vehicle")

    def change_gear(self):
        print("Vehicle changes 7 gears")

class Car(Vehicle):

    def max_speed(self):
        print("Max speed in 240 for car")

    def change_gear(self):
        print("car changes 7 gears")


