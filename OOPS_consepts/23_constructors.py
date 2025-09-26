"""class student:

    def __init__(self,name,roll_no,branch):

        self.name=name
        self.roll_no=roll_no
        self.branch=branch

    def get_name(self):
        return self.name

    def get_info(self):
            print(f"the name of a student is:",{self.name},"roll no is:",{self.roll_no},"branch is:",{self.branch})



s=student("sakshi",61,"Data science")

print(s.get_name())
s.get_info()"""


class dog:

    def __init__(self,name="unkown",breed="mixed"):
        self.name=name
        self.breed=breed

    def dog_info(self):
        print(f"name is:",{self.name},"breed:",{self.breed})


dog1= dog()
dog1.dog_info()

dog2=dog("max")#python fetch max as a name, because there is only one parameter passed: op is= max & mixed
dog2.dog_info()


dog3=dog("bella","labrador")        
dog3.dog_info()