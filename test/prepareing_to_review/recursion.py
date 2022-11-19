def privet(x):
    if x == 0:
        return
    else:
        print('hello world')
        privet(x-1)

privet(3)

def sum(x):
    if x == 0:
        return 0
    else:
        return x + sum(x-1)

z = sum(6)  # x + sum(x - 1)
# 1.)6 + 5                                  = 11
# 2.)  (6-1) + 4                            = 4
# 3.)         (5-1) + 3                     = 3
# 4.)               (4-1) + 2               = 2
# 5.)                     (3-1) + 1         = 1
# 6.)                           (2-1) + 0   = 0
#                                         --------      21
print(z)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
a = factorial(5)


print(a)


def fibonacci(q):
    if q == 0:
        return 0
    elif q == 1:
        return 1
    else:
        return fibonacci(q-1) + fibonacci(q-2)


fib = fibonacci(13)  # fibonacci(q-1) + fibonacci(q-2)=
# 1.)                           (7                       +                       6)
# 1.)               (6           +           5)                     (5           +           4)
# 1.)         (5     +     4)         (4     +     3)         (4     +     3)         (3     +   2)
# 1.)     (4+3)+(3+2) (3+2)+(2+1) (3+2)+(2+1) (2+1)+(1+0) (3+2)+(2+1) (2+1)+(1+0) (2+1)+(1+0)
print(fib)





