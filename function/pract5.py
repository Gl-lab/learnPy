
def elements_count(mas):
    dictionary = dict()
    for word in mas:
        value = dictionary.get(word,-1)
        if value == -1:
            dictionary.update({word: 1})
        else:
            dictionary.update({word: value + 1})
    count = 0
    for value in dictionary.values():
        if value > 1: 
            count += 1
    return count


sequence = input().split() 
print(elements_count(sequence))