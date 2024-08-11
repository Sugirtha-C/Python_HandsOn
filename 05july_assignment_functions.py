"""
find the largest number in the given list
"""
x= [4,6,8,24,12,2]
x.sort(reverse=True)
print("Largest number after sorting the given list is" ,x[0])

"""
Assign a different name to function and call it through the new name
Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
Given:
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
"""
def show_student(name, age):
    print(name, age)

show_student("Ian Maccabe", 40)

"""
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
A recursive function is a function that calls itself again and again.
Expected Output:
55
"""
def sumOfNumbers(i):
    if i == 0:
        return 0
    else:
        return i + sumOfNumbers(i - 1)

result=sumOfNumbers(10)
print(result)

"""
Create an inner function to calculate the addition in the following way:
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
"""
def outerFunction(a,b):
    def innerFunction(a,b):
        sum = a + b
        return sum

    result_variable=innerFunction(a,b)
    final_result = result_variable + 5
    return final_result

final_result=outerFunction(5,5)
print(final_result)

"""
Return multiple values from a function
Write a program to create function calculation() such that it can accept two variables 
and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
Given:
def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
Expected Output
50, 30
"""

def calculation( a, b):
    sum= a+b
    difference = a -b
    return sum, difference

result_sum, result_difference= calculation(40,10)
print(result_sum, result_difference)
