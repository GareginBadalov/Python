from sys import argv
from functools import reduce
from itertools import cycle, count
import math

def func1():
    path, a, b, c = argv
    return (int(a) * int(b)) + int(c)


print(func1())


def func2(a):

    return [x for x in a[1::] if a[a.index(x)] > a[a.index(x)-1]]


print(func2([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))


def func3():
    return [x for x in range(20, 241, 1) if x % 20 == 0 or x % 21 == 0]


print(func3())


def func4(a):
    return [x for x in a if a.count(x) == 1]


print(func4([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))


def func5(a, b):
    return a * b


print(reduce(func5, [x for x in range(100, 1001) if x % 2 == 0]))


def func6_1(a):
    b=[]
    for i in count(a):
        if i > 10:
            break
        else:
            b.append(i)
    return b


print(func6_1(3))


def func6_2():
    c = 0
    b = []
    for a in cycle([1, 2, 3]):
        if c > 8:
            break
        b.append(a)
        c += 1
    return b


print(func6_2())


def func7(n):
    for x in range(1, n):
        x = math.factorial(x)
        yield x


for i in func7(7):
    print(i)