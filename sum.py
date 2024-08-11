def sum():
    for i in range(0,10):
        if(i == 0):
            previous_number = 0
        else:
            previous_number= i - 1
        sum= i + previous_number
        print('Current Number: ' , i ,' Previous Number: ', previous_number,'Sum:' , sum)


sum()