"""Конечно, можно вкладывать декораторы друг в друга, например так:"""
def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper

def sandwich(food="--ветчина--"):
    print(food)

sandwich()# выведет: --ветчина--
print("--------------------")
sandwich = bread(ingredients(sandwich))
sandwich()  # выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>
print("--------------------")

"""И используя синтаксис декораторов:"""
@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)

sandwich()  # выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

"""Следует помнить о том, что порядок декорирования ВАЖЕН:"""
@ingredients
@bread
def sandwich(food="--ветчина--"):
    print(food)

sandwich()  # выведет:
# #помидоры#
# </------\>
# --ветчина--
# <\______/>
# ~салат~