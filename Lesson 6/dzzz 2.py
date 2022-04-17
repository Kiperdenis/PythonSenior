class Hero:
    def __init__(self,name,age,power,race):
        self.name = name
        self.age = age
        self.power = power
        self.race = race
    def show(self):
            print(self.age)
            print(self.name)
            print(self.power)
            print(self.race)
first_hero = Hero(name=input("Enter name: "),age=input("Enter age: "),power=input("Enter power: "),race=input("Enter race: "))
first_hero.show()
second_hero = Hero(name=input("Enter name: "),age=input("Enter age: "),power=input("Enter power: "),race=input("Enter race: "))
second_hero.show()
third_hero = Hero(name=input("Enter name: "),age=input("Enter age: "),power=input("Enter power: "),race=input("Enter race: "))
third_hero.show()

