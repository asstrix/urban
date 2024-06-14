class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.end, 2):
            self.start += 2
            return i
        raise StopIteration()


k = EvenNumbers(10, 25)
print(*k, sep='\n')
