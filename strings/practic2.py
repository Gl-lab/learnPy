#С клавиатуры вводится строка, а затем - подстрока. В строке найти все слова, в которых содержится заданная подстрока, и вывести эти слова целиком.

inputString = input()
findString = input()

wordList = inputString.split(' ')

for word in wordList:
    if word.lower().find(findString.lower()) >= 0:
        print(word)
