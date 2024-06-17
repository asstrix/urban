import math


def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res <= 1:
            print('Neither Composite nor Simple')
        elif res == 2:
            print('Simple')
        else:
            for i in range(2, int(math.sqrt(res)) + 1):
                if res % i == 0:
                    print('Composite')
                    break
            else:
                print('Simple')
        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
