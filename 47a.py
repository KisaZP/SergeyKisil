x = float(input('Введите х'))
y = float(input('Введите у'))
z = float(input('Введите z'))
if (x + y > z) and (x + z > y) and (y + z > x):
    print('Существует')
else:
    print('Не существует')