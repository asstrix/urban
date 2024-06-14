from random import randint
from termcolor import colored
from colorama import init



class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0
        self.house = None

    def __str__(self):
        return f'I\'m {self.name}, fullness: {self.fullness}, food left: {self.food}, money left: {self.money}'

    def eat(self):
        if self.food >= 10:
            print(f'{self.name} ate')
            self.fullness += 10
            self.food -= 10
        else:
            print(f'{self.name} no food')

    def work(self):
        print(colored(f'{self.name} worked', 'magenta'))
        self.money += 50
        self.fullness -= 10

    def play(self):
        print(colored(f'{self.name} was playing whole day long', 'green'))
        self.fullness -= 10

    def shop(self):
        if self.money >= 50:
            print(f'{self.name} went to a supermarket')
            self.food += 50
            self.money -= 50
        else:
            print(f'no money')
            
    def move_to_house(self, house):
        self.house = house
        print(colored(f'{self.name} moved to house','cyan'))
    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} died')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shop()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50





vasya = Man(name='Vasya')
misha = Man(name='Misha')
for day in range(1, 21):
    print(colored(f'**************** {day} ****************', 'yellow'))
    vasya.act()
    misha.act()
    print(misha)
    print(vasya)
