#Написать скрипт, который считывает с клавиатуры числа, складывает только четные и выводит результат на экран.

string = ''
sum = 0
a = True
while True:
    string = input()
    if string == '':
        break
#    if string.isnumeric():
    convertedChar = int(string)
    if convertedChar % 2 == 0:
        sum += convertedChar
print(sum)


