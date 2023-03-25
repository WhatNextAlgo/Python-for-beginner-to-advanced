x = 3
y = x
print(id(x),id(y))
y = 4
print(id(x), id(y))


colours1 = ["red", "blue"]
colours2 = colours1
print(colours1, colours2)
print(id(colours1),id(colours2))
colours2 = "green"
print(colours1,colours2)

colours1 = ["red", "blue"]
colours2 = colours1

colours2[1] = "green"
print(colours1,colours2)

#Copying Lists

firstnames = ['Kevin', 'Jamina', 'Lars', 'Maria']
whatever = ["Kevin", "Pythonista", 7.8, [3.54, "rkm"]]

#Problems of Copying Lists
print()
person1 = ["Swen", ["Seestrasse", "Konstanz"]]
person2 = person1.copy()
person2[0] = "Sarah"
print(person1,person2)
person2[1][0] = "Bücklestraße"
print(person1,person2)

#deepcopy from the Module copy

from copy import deepcopy
person1 = ["Swen", ["Seestrasse", "Konstanz"]]

person2 = deepcopy(person1)
print(id(person1[1]), id(person2[1]))
person2[0] = "Sarah"
print(person1,person2)
person2[1][0] = "Bücklestrasse"
print(person1,person2)

