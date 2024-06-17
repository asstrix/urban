import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill

    def run(self):
        enemies = 100
        day = 0
        print(f'{self.name}, we are under attack!')
        while enemies > 0:
            enemies -= self.skill
            day += 1
            print(f'{self.name} fights {day} day, enemies left: {enemies}')
            time.sleep(0.5)
        print(f'{self.name} won after {day} days!')


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
time.sleep(0.1)
knight2.start()
knight1.join()
knight2.join()
