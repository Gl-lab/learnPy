import json

def age_count(obj):
    dictionary = dict()
    newobj = json.loads(obj)
    mas = newobj.get('workers')
    for item in mas:
        occupation = item.get('occupation')
        value = dictionary.get(occupation,[])
        if value == []:
           dictionary.update({occupation: [item.get('age')]}) 
        else:
           value.append(item.get('age'))
           dictionary.update({occupation: value}) 
    result = dict()
    for key, arr in dictionary.items():
        sum = 0
        for x in arr:
            sum += x
        result.update({key: sum/len(arr)})
    outputFile = open('age.json','w')
    outputFile.write(json.dumps(result))
    print(result)

with open("input.txt") as f: 
    age_count(input())