class House:

    def __init__(self, numberOfFloors, step, color):
        self.numberOfFloors = 10
        self.step = step
        self.color = color

    for steps in numberOfFloors():
        numberOfFloors -= 1
        print(steps)


house = House('Текущий этаж равен', 10, 'желтый')
print(house.numberOfFloors)
print(house.step)
print(house.color)



# class House:
#
#
#     def __init__(self, numberOffFloors, color, step, door):
#         self.numberOffFloors = 0
#         self.color = color
#         self.step = step
#         self.door = door
#
#
#     def setNewNumberOffFloors(self, floors):
#         self.numberOffFloors = floors
#         print(self.numberOffFloors)
#
# house = House('маленкий', 'серый', 8, 'деревянные')
# print(house.step)
# print(house.color)
# print(house.door)
