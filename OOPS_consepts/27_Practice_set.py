"""#   Q1
class Car:

    def drive(self):
        print("car is moving")

c=Car()
c.drive()

#Q2
class Person:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def info(self):
        print(f"name is: {self.name} age is: {self.age}")

p=Person("sakshi",20)
p.info()"""

#Q3 multilevel inheritance
class Livingbeing:
    def L(self):
        print("this is class livingbeing")

class Animal(Livingbeing):
    def A(self):
        print("this is animal class")

class Dog(Animal):
    def D(self):
        print("this is dog class")


Q=Dog()
Q.L()
Q.A()
Q.D()
        


        