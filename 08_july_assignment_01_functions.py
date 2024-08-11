"""
Exercise 1: Positional and Keyword Arguments
Create a function called calculate_area that calculates the area of a rectangle. T
he function should accept two arguments: length and width.
Use both positional and keyword arguments to call the function
"""

def calculateArea(length, width):
    area=length * width
    return area

area=calculateArea(25,30)
print("Area of rectangle: Positional argument function call: " ,area)

area_2=calculateArea(length=24, width=45)
print("Area of rectange:Keywrod argument function call: ",area_2)

"""
Exercise 2: Default Arguments
Create a function called greet that prints a greeting message. 
The function should have a default argument name with the default value "Guest".
"""

def greet(name="Guest"):
    print("Hello ", name)

print("Printing with an argument:")
greet("Jaime Lannister")
print("Printing with default argument value:")
greet()

"""
Exercise 3: Variable-Length Arguments
Create a function called calculate_sum that accepts any number of arguments and returns their sum. 
Use the *args syntax to handle a variable number of arguments.
"""

def calculate_sum(*args):
    sum=0
    for value in args:
        sum+=value
    return sum

args_sum_3_values=calculate_sum(4,5,6)
print("output using *args with 3 arguments is:" , args_sum_3_values)

args_sum_6_values=calculate_sum(4,5,6,9,995,625)
print("output using *args with 3 arguments is:" , args_sum_6_values)

"""
Exercise 4: Mixed Arguments
Create a function called create_profile that accepts the following arguments:
first_name and last_name as positional arguments.
age as a keyword argument with a default value of None.
Any number of additional keyword arguments to store other details about the profile using **kwargs.
"""

def create_profile(first_name, last_name, age=None,**kwargs):
    print("Some interesting casts from the show are:")
    print("first_name = " ,first_name)
    print("Last name = ",last_name)
    print("Age = ",age)
    for key,value in kwargs.items():
        print(f"{key} = " , value)

create_profile("Cersei", "Lannister",45,place="Kings Landing",role="Evil")
create_profile("Jon Snow", "Targerian",34,place="Winterfell")
create_profile("Khal", "Drogo",place="Westeros")

"""
Exercise 5: Combining All Types of Arguments
Create a function called order_pizza that accepts the following arguments:
size as a positional argument.
crust as a keyword argument with a default value of "regular".
Any number of additional toppings using *args.
Additional options using **kwargs.
"""

def order_pizza(size,crust="Regular",*args,**kwargs):
    print("Size required in inches:" , size)
    print("Crust selected: " , crust)
    for topping in args:
        print("Toppings added:" , topping)
    for key,value in kwargs.items():
        print(f"{key} :" , value)

print("Customer ID:101")       
order_pizza(size=7, crust="Pan Crust",Toppings="Olive, Jalapeno,Mushroom",Extras="Cheese Burst")
print("Customer ID:102")
order_pizza(size=12, crust="Thin Crust",Toppings="Corn,Jalapeno,Mushroom",Extras="More Jalapenos",Message="Happy Birthday To You")
print("Customer ID:103")
order_pizza(size=7,Toppings="Jalapenos",Excluded = "No raw onions",Message="Happy Birthday To You")


