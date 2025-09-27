class Animal: #parent class(super class)
    location="australia"
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("generic animal sound")

class Dog(Animal):#child class(subclass)

    def speak(self):
        super().speak()#calling super classz speak method
        print("woof!")

a=Animal("Dog")
d=Dog("BRUNO")
d.speak()
#print(d.location)