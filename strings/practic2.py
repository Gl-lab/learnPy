#С клавиатуры вводится строка, а затем - подстрока. В строке найти все слова, в которых содержится заданная подстрока, и вывести эти слова целиком.

inputString = input('Ввеите строку: ')
findString = input('Введите подстроку: ')

wordList = inputString.split(' ')

for word in wordList:
    if word.find(findString) >= 0:
        print(word)
