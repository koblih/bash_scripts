# create class furniture
# teakwood should be type of furniture in base class
# create class called chair that inherits from class furniture
# gice user option to change type of wood for the chair
# number of legs on a chair cannot be changed

class Furniture:
    wood_type = 'Teakwood'


class Chair(Furniture):
    legs_number = 4

    def change_wood_type(self):
        self.wood_type = input()
        return self.wood_type

furniture = Furniture()
chair = Chair()
print(furniture.wood_type)
print(chair.legs_number)
new_wood_type = chair.change_wood_type()
print(chair.wood_type)
