strin = input('Введите строку:')
b = len(strin)
if b > 10:
    print(strin[0:7])
else:
    strin = list(strin)
    p = (12 - b) + 1
    for x in range(1, p):
        strin.append('0')
    strin = str(strin)
    print(strin)