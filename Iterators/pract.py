dictionary = dict()
string = input()
mas = string.replace(' ',',',-1).split(',',)
for word in mas:
    if word != '':
        value = dictionary.get(word,-1)
        if value == -1:
            dictionary.update({word: 1})
        else:
            dictionary.update({word: value + 1})
print(dictionary)