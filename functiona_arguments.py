#default arguments
def student(name, age, grade='Five',school="ABC"):
    print("student details:", name, age, grade, school)

student("john",10, 'Six')


#keyword arguments -
def student1(name, age):
    print('Student details: ', name, age)

#default call
student(name='John',age=10)
student1(age=30,name='Tyrion')
student1("Sansa",age=30)

#positional arguments-values get assigned to arg by their position when its called
#1.default arguments should follow non default arguments

def get_students(name,age,grade="five"):
    print(name,grade, age)

get_students("Arya Stark", age=5)
#keyword argument should follow positional arg only

#variable length arguments
#*args -> arbitary positional args-- considered like tuples
#**kwargs -> arbitary keyword args(named args and functions) -- considered like dictionary: keyword and value

def percentage(s1,s2,s3):
    avg=(s1+s2+s3)/3
    print("average: ", avg)

percentage(10,20,30)

def average(*args):
    sum=0
    for i in args:
        sum+=i
    print ("average is", sum/len(args))

average(10,20,30,40)

#kwargs:
#use the unpacking operator

def percentage2(**kwargs): #considered like a key value pair
    sum=0
    for sub in kwargs:
        #get argument name
        sub_name=sub #sub is like keys
        #get argument value
        sub_marks=kwargs[sub] #calling like dict name[key] : kwargs[sub] will give value
        print(sub_name,'=',sub_marks)
        sum+=sub_marks

percentage2(phy=10,chem=20,maths=30)


def create_profile(first_name, last_name, age=None, **kwargs):
    profile = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
    }
    profile.update(kwargs)
    return profile
# 1. With all arguments
profile1 = create_profile("John", "Doe", age=30, location="New York", profession="Engineer")
print(profile1)