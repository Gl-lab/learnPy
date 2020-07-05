#С клавиатуры вводится строка. В строке заменить пробелы звездочкой. 
# Если встречается подряд несколько пробелов, то их следует заменить одним знаком "*", пробелы в начале и конце строки удалить.

string = input('Введите строку: ')
outputString = string.strip().replace(' ','*',-1)
while (outputString.find('**') != -1):
    outputString = outputString.replace('**','*')
print(outputString)