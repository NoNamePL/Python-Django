first_set = input("Введите список слов: ")
first_set = set(first_set.split(","))
count_first_set = len(first_set)

second_set = input(f"Количество слов в 1 списке: {count_first_set}, Введите"
                    " 2-ой список с таким же количеством символов: ")

second_set = set(second_set.split(","))

dictinaru = {}

for count in range(count_first_set):
    dictinaru = dict(zip(list(first_set),list(second_set)))
#   [second_set[count]] = first_set[count]


print(dictinaru)