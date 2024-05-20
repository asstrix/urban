class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building1 = Building(10, "flat")
building2 = Building(10, "house")

print(building1 == building1)  # True
print(building1 == building2)  # False