#  1
def math(arg):
    if arg == 'add':
        def add(x, y):
            return x + y
        return add
    elif arg == 'substract':
        def sub(x,y):
            return x - y
        return sub

task1 = math('add')
task12 = math('substract')
print(task1(5, 6))
print(task12(5, 6))


#  2
task2 = lambda x: x ** 2
# print(task2(2))

def sqrt(n):
    return n ** 2

print(sqrt(2))

#  3
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

task3 = Rect(4, 8)
print(task3())
