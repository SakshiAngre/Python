class Employee:

    company="cisco"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    #instance method
    def info(self):
        return f"name of emp is:{self.name},salary is:{self.salary}"

e=Employee("gorge",830043)
e1=Employee("Genelia",832435)
print(Employee.company)
print(Employee.name)#throw error because, it is instance attribute ans i am trying to access it with class name
