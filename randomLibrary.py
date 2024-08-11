import random

print(random.randint(0,9))
print(random.randint(0,9))
print(random.randint(0,9))

#length 4

print(random.randint(1000,9999))

#create random number of length 4 with step of 2 which starts from 1000, stops at 10,000

print(random.randrange(1000,10000,2))
randomList=[]
for i in range(0,10):
    randomList.append(random.randint(0,100))

print(randomList)

#create unique random numbers

num_list=random.sample(range(0,100),10)
print(num_list)

print(random.uniform(10.75,75.25)) #return float randomnumbers

random_floatList=[]
for i in range(0,10):
    x=round(random.uniform(50.0, 500.0),2)
    random_floatList.append(x)

print(random_floatList)

random_float_listComprehension=[round(random.uniform(50.0,60.0),2) for i in range(0,10)]
print(random_float_listComprehension)


def gen_random_numbers(length, start, stop,step):
    random_numbers=[random.randrange(start,stop,step) for i in range(length)]
    return random_numbers

rand_num=gen_random_numbers(10,23,50,3)
print(rand_num)