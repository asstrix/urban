list_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def multiply(n):
    return n ** 2


def is_odd(n):
    return n % 2


print(list(map(multiply, filter(is_odd, list_))))

