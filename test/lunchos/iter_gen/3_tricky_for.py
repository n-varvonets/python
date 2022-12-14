l = [1, 2, 3, 4]


class MyCustomNotIterClass:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


not_iter_obj = MyCustomNotIterClass(2)
# print(next(not_iter_obj))
# 1)что бьі сделать итерируемьій КАСТОМНЬІЙ обьект - нужно доавить итер
iterator = iter(not_iter_obj)
# 2) что бьі сделать генератор - нужно ему придать функцию __next__ - наврное єто и делать yield
print(next(iterator))