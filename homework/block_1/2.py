input_string = input("Введите строку: ")

if "С" in input_string or 'c' in input_string:
    print("Буква 'С' или 'с' есть в введённой строке")
#elif 'с' in input_string:
#    print("Буква 'с' есть в введённой строке")

for letter in input_string:
    if len(input_string) > 3:
        if letter == input_string[2]:
            continue

    if letter == input_string[-1]:
        break
    print(letter, end="")


cout_letter = len(input_string)
print("\nКоличество букв:", cout_letter)
