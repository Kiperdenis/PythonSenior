class Hero:
    def __init__(self,name):
        self.name = name
class Dobry:
    def __init__(self,dobra):
        self.dobra = dobra
        self.herod = []
    def add_hero(self,hero):
        self.herod.append(hero)
    def print_hero(self):
        if self.herod != []:
            print(f"Ім'я {self.dobra} героя: ")
            for i in self.herod:
                print(i.name)
        else:
            print(f"Немає такого героя {self.dobra}")
class Pogany:
    def __init__(self,pogana):
        self.pogana = pogana
        self.herop = []
    def add_hero(self,hero):
        self.herop.append(hero)
    def print_hero(self):
        if self.herop != []:
            print(f"Ім'я  {self.pogana} героя: ")
            for i in self.herop:
                print(i.name)
        else:
            print(f"Немає такого героя {self.pogana}")
first_hero = Hero("Jack")
second_hero = Hero("Nick")
herodo = Dobry('доброго')
herodo.add_hero(first_hero)
herodo.print_hero()
heropo = Pogany("поганого")
heropo.add_hero(second_hero)
heropo.print_hero()

