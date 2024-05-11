class House:

    def __init__(self):
        self.numberOfFloors = 10

    def cur_floor(self):
        for i in range(1, self.numberOfFloors + 1):
            print('Текущий этаж равен:', i)


house = House()
house.cur_floor()
