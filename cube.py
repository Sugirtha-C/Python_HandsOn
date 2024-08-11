def cube(limit):
    for i in range(limit):
        cubed=i ** 3;
        print('Current Number is : ', i ,'and the cube is: ', cubed)

print("Enter the number until which you require the cube value")
limit=int(input())
cube(limit)