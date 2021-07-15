foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

filter1 = list(filter(lambda x: x % 3 == 0, foo))
print(filter1)

print(list(map(lambda x: x*3+20, foo)))

# ---------------------------------------------------------------------------------------------------

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

simple_iter = SimpleIterator(3)

for i in simple_iter:
    print(i)

# ----------------------------------------------------------------------------------------

numbers = range(10)
squared = [n ** 2 for n in numbers if n % 2 == 0]
print(squared)   # [0, 4, 16, 36, 64]

print(hash(3.7))
print(hash(3.7))
print(hash(3.71))