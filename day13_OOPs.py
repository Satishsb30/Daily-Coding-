"""Create a Class:

Write a class Mobile with attributes brand and price.
Create two objects of the class and display their attributes using a method.
Method Definition:

Define a class Student with attributes name and marks.
Write a method display_info() that prints the student's name and marks.
Create multiple objects of the Student class and call the method on each.
"""
# create class
class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)

# create two objects
mobile1 = mobile("Oneplus",200000)
mobile2 = mobile("Nokia",68784)

# displaying attributes
mobile1.display()
mobile2.display()
"""Define a class Student with attributes name and marks.
Write a method display_info() that prints the student's name and marks.
Create multiple objects of the Student class and call the method on each.
"""
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display_info(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)
# 3rd line
student1 = student("Satish",525)
student2 = student("Alexa0", 541)

student1.display_info()
student2.display_info()


# dwerfg
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.brand} accelerated. Current speed: {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"{self.brand} slowed down. Current speed: {self.speed} km/h")

# Example Usage
car1 = Car("Toyota")

car1.accelerate(20)
car1.accelerate(30)
car1.brake(25)
car1.brake(50)
