def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    return reverse


# Taking input from the user
number = int(input("Enter a positive integer to reverse: "))
reversed_number = reverse_number(number)
print(f"The reversed number of {number} is {reversed_number}")
