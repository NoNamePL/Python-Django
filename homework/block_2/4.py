first_word = input("Введите слово: ")
second_word = input("Введите слово: ")
third_word = input("Введите слово: ")

print("Слова в нижнем регистре", first_word.lower(), second_word.lower(), third_word.lower())
print("Слова в верхнем регистре", first_word.upper(), second_word.upper(), third_word.upper())
print("Первая буква заглавная", first_word.capitalize(), second_word.capitalize(), third_word.capitalize())
print("8 штук {}, 9 штук {}, 2 штуки{}".format(first_word,second_word,third_word))