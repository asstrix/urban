immutableVar = (10.00, 7631, 'demo', True)
print('Immutable tuple:', immutableVar)
#immutableVar[3] = False # Will fail due to tuples don't support item assignment
mutableList = [10.00, 6840, 'real', False]
mutableList[3] = True
print('Mutable list:', mutableList)
