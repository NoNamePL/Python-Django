input_string = input("Введите строку: ")

if "С" in input_string or 'c' in input_string:
    print("Буква 'С' или 'с' есть в введённой строке")
#elif 'с' in input_string:
#    print("Буква 'с' есть в введённой строке")
counter = 0
cout_string = len(input_string)

for letter in input_string:
    counter += 1
    if len(input_string) > 3:
        if counter == 3:
            continue

    if counter == cout_string:
        break
    print(letter, end="")
    
print("\nКоличество букв:", cout_string)
