class Employee:

    company="cisco"

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    #instance method(default)
    def info(self):
        return f"name of emp is:{self.name},salary is:{self.salary}"
        print(info)

    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.comapany=new_company


e=Employee("gorge",830043)
e1=Employee("Genelia",832435)
print(Employee.company)
#print(Employee.name)#throw error because, it is instance attribute ans i am trying to access it with class name
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)