data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calc_int(data, summ=0):
    for i in data:
        if isinstance(i, str):
            summ += len(i)
        elif isinstance(i, int):
            summ += i
        elif isinstance(i, (list, tuple, set)):
            summ = calc_int(i, summ)
        elif isinstance(i, dict):
            summ = calc_int(i.keys(), summ)
            summ = calc_int(i.values(), summ)
    return summ


print(calc_int(data_structure))