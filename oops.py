
#instance variables - : can ahve access of both class and object attri, can modify object state
# attached to instance of class, defined inside constructor(inside init method of class)
#class variables -  ony upto class attr, can modify class's object state
#sttaic: no access to both class and instance variables/methods

class Student:
    #class variable
    school = "ABC school"

    #constuctor
    def __init__(self,name,age, grade):

        #instance variables
        self.name=name
        self.age=age
        self.grade=grade

    def show(self):
        print(self.name,self.age, self.grade)
    @classmethod #used to access and modify class variables
    def change_school(cls,new_school):
        cls.school=new_school

    @staticmethod #doesnot have access to instance and class variables
    def hello():
        print("hello")

    @classmethod
    def showSchool(cls):
        print("School name is: ", Student.school)

 #use objects to access the instancr variables
s=Student("Raghu",8,"three")
#print(s.name, s.age, s.grade)
# print('School name:', Student.school) : Access class attribute with class name
Student.showSchool()
s.show()
s.change_school("XYZ school")
Student.showSchool()

#call static method using the class name
Student.hello()

""""
#inside class: 3 types of methods
1)Instance methods
2)class method
3)Static method

"""
class Person:

    def __init__(self,name,age,profession):
        self.name=name
        self.age=age
        self.profession=profession

    def show(self):
        print("Name" , self.name, 'Sex:', self.sex , 'Profession :' ,self.profession)

    def work(self):
        print(self.name, 'is working at', self.profession)

S1=Person('sugirtha','Female','Data')
S1.show()
S1.work()

