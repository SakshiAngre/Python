class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @property
    def first_name(self): #getter
        l=self.name.split(" ")
        return l[0]
    
    @first_name.setter  #setter
    def first_name(self,first):#for update name
        l=self.name.split(" ")
        new_name=f"{first} {l[1]}"#l[1] beacause split() func converts string to list so l[1]=doe    
        self.name=new_name

e=Employee("mrinalini doe",550000)
#e.projects=6
#print(e.projects)
print(e.first_name)
e.first_name="jasmin"
print(e.name)

