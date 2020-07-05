#Написать скрипт, который считывает с клавиатуры числа, складывает только четные и выводит результат на экран.

string = ''
sum = 0
string = input('Введите числа:')
mass = string.split(' ')
for char in mass:
    if char.isdigit():
        convertedChar = int(char)
        if convertedChar % 2 == 0:
            sum += int(convertedChar)
print('Сумма четных:', sum)