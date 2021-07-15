def sum(x):
    if x == 0:
        return 0
    else:
        return x + sum(x-1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(q):
    if q == 0:
        return 0
    elif q == 1:
        return 1
    else:
        return fibonacci(q-1) + fibonacci(q-2)


z = sum(5)
print(z)
a = factorial(5)
print(a)
fib = fibonacci(30)
print(fib)

