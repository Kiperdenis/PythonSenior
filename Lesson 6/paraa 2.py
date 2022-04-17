class Student:
    print("Hi!")
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("I am Alive!")
    def show(self):
        print(self.age)
        print(self.name)
        
first_student = Student(name=input("Enter name: "),age=13)
first_student.show()
second_student = Student(name="Sahar",age=12)
second_student.show()






















