number = int(input('Введите число: '))
print(f"\n{number}")
count = number - 1

while count >= 0:
    for i in range(-number, number + 1):
        if abs(i) > count:
            print(abs(i), end='')
        elif i == 0:
            print(end='')
        else:
            print('.', end='')
    count -= 1
    print()
