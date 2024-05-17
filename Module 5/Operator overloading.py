class Building:

    def __init__(self):
        self.numberOfFloors = 3
        self.buildingType = 'flat'

    def __eq__(self, **kwargs):
        return self.numberOfFloors == self.buildingType


flat = Building()
if Building.__eq__(self=flat):
    print('equal')
else:
    print('not equal')

