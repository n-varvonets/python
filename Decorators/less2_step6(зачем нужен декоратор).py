"""Использовать декораторы для расширения различных функций одним и тем же кодом,
без повторного его переписывания каждый раз, например:"""

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time

    def wrapper(*args, **kwargs):
        t = time.process_time()
        res = func(*args, **kwargs)
        print(func.__name__, time.process_time() - t)
        return res

    return wrapper

def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper

@benchmark
@logging
@counter
def reverse_string(string):
    return str(reversed(string))


print(reverse_string("А роза упала на лапу Азора"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni,"))
print('---------------------1------------------')

# выведет:
# reverse_string ('А роза упала на лапу Азора',) {}
# wrapper 0.0
# reverse_string была вызвана: 1x
# арозА упал ан алапу азор А
# reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag,a canal: Panama!',) {}
# wrapper 0.0
# reverse_string была вызвана: 2x
# !amanaP :lniaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,el,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A


# --------------------------------------------------------------------------------------------------------------
"""Таким образом, декораторы можно применить к любой функции, расширив её функционал и не переписывая ни строчки кода!"""

import http.client

@benchmark
@logging
@counter
def get_random_futurama_quote():
    conn = http.client.HTTPConnection("slashdot.org:80")
    conn.request("HEAD", "/index.html")
    for key, value in conn.getresponse().getheaders():
        if key.startswith("x-b") or key.startswith("x-f"):
            return value
    return "Эх, нет... не могу!"

print(get_random_futurama_quote())
print(get_random_futurama_quote())

# outputs:
# get_random_futurama_quote () {}
# wrapper 0.02
# get_random_futurama_quote была вызвана: 1x
# The laws of science be a harsh mistress.
# get_random_futurama_quote () {}
# wrapper 0.01
# get_random_futurama_quote была вызвана: 2x
# Curse you, merciful Poseidon!

"""В Python включены такие декораторы как property, staticmethod и т.д. В Django декораторы используются для 
управления кешированием, контроля за правами доступа и определения обработчиков адресов."""

