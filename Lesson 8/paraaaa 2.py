import random
class Human:
    def __init__(self,name = "Human",job = None,home = None,car = None):
        self.name = name
        self.money = 100
        self.gledness = 50
        self.setiety = 50
        self.job = job
        self.home = home
        self.car = car
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def day_index(self):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass
class Auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.color = brand_list[self.brand]["color"]
class House:
    def __init__(self):
        self.food = 0
        self.mess = 0
class Job:
    def __init__(self,job_list):
        self.job = random.choise(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladnees_less = job_list[self,job_list]["gladness_less"]
brands_of_car  = {
    "BMW": {"color":"Black"},
    "Mercedes": {"color":"Grey"},
    "Ferari": {"color":"Red"},
    "Lamborgini": {"color":"Yellow"}
}
job_list = {
    "Python Developer": {"salary":40,"gladnees_less":3},
    "Teacher": {"salary":25,"gladnees_less":25},
    "Game Developer": {"salary":40,"gladnees_less":3},
}