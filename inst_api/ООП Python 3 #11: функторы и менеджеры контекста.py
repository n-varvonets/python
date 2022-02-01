class Person:
    def __init__(self, surname, forename, old):
        self.surname = surname
        self.forename = forename
        self.old = old

    def __repr__(self):
        return f'{self.surname}, {self.forename}, {self.old}'
#
class Sortkey:
    def __init__(self, lst_objs_person):
        self.lst_objs = lst_objs_person

    def __call__(self, *args, **kwargs):
        sorted([rec.old for rec in self.lst_objs])
        return print(self.lst_objs)
        sorted(self.lst_objs, key=lambda recieved_args:)
        for rec in self.lst_objs:

                    rec[0]

        print(self, *args)
p = [Person('Varvonets','Nick', 25), Person('Varvonets','Alex', 29,), Person('Varvonets','Anatoliy', 24)]
data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]

data.sort(key=lambda x:x[0])
print(data)
