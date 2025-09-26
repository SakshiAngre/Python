class Employee:
    company = "INTEL"

    def get_sal(self):
        return 599999
    

e=Employee() #object
print(e.get_sal())

e1=Employee()
print(e1.get_sal())
print(e1.company)