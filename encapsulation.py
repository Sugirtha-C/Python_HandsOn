#data bundling in single unit
#example is 'Class' :Traps datas and methods working on single unit

class Employee:

    def __init__(self,name, salary,project):
        self.name=name
        self.__salary=salary
        self.project=project

    def work(self):
        print(self.name, "is working on", self.project)

    def show(self):
        print("name",self.name)
        print("Salary", self.__salary)
        print("project", self.project)

emp1=Employee("John",75 ,"GMS")
emp1.work()
emp1.show()