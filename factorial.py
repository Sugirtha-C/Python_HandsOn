def factorial(value):
  result = 1
  i: int
  for i in range(1, value + 1 ):
      result=result * i

  return result

print('Enter the number to calculate factorial:')
value=int(input())
output=factorial(value)
print('Factorial is: ' , output)