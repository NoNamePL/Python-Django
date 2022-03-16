first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

if first_number < second_number:
    print("Первое число меньше пограничного")
elif first_number >= second_number:
    print("Второе число меньше пограничного")
if first_number > second_number * 3:
    print("Первое число больше пограничного в 3 раза")
