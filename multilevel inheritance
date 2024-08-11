class person:

    def person_info(self,name,age):
        self.name=name
        self.age=age
        print("person info")
        print('Name' ,name, 'Age', age)

class Company(person):

    def company_info(self,company_name,location):
        print("company name")
        print('Company name: ', company_name , 'location is:' , location)

class Employee(Company,person):

    def employee_info(self,emp_id):
        print("Employee name is:" , self.name ,"age is:", self.age, "id is:", emp_id)

emp=Employee()
emp.person_info("john",56)
emp.company_info("TCS","Chennai")
emp.employee_info(101)

class company:

    def company_name(self):
        return "tcs"

class Employee(company):

    def info(self):
        c_name=super().company_name()
        print("company name is: " , c_name)

emp1=Employee()
emp1.info()

