import math
AB = input("Длина первого катета: ")
AC = input("Длина второго катета: ")
AB = float(AB)
AC = float(AC)
BC = math.sqrt(AB ** 2 + AC ** 2)
S = (AB * AC) / 2
print('Гипотенуза:', BC)
print('Площадь', S)