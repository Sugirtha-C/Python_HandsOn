class Student:

    def __init__(self,name,age):
        self.name= name
        self.__age=age

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age=new_age

S1=Student("john",23)
print(S1.get_age())
S1.set_age(25)
print(S1.get_age())


