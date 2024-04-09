myList = ['January', 'February', 'March', 'April', 'May', 'June']
print('List:', myList)
print(f'First element: {myList[0]}\nLast element: {myList[-1]}')
print('Sublist:', myList[2:5])
myList[2] = 'December'
print(f'Modified list: {myList}\n')

myDict = {'список': 'list', 'кортеж': 'tuple', 'словарь': 'dictionary', 'множество': 'set'}
print('Dictionary:', myDict)
print('Translation:', myDict['список'])
myDict['массив'] = 'array'
print('Modified dictionary:', myDict)