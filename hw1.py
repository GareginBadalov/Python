        ###   Задание 1   ###
def func1():
    a = int(input('Введите число'))
    b = input('Введите строку')
    print(a, type(a), b, type(b))
    return a, b
func1()


        ##   Задание 2   ###
def func2(n):
    h = int((n / 60 ** 2) // 1)
    m = int((n - h * 3600) // 60)
    s = int(n - (h * 3600 + m * 60))
    print(f'{h}:{m}:{s}')
func2(7722)

        ##   Задание 3   ###
def func3(n):
    n = str(n)
    d = int(n)+int((n+n))+int((n+n+n))
    print(d)

func3(3)
        ##   Задание 4   ###
def func4():
    n = int(input("Введите"))
    maxi = n % 10
    n = n // 10
    while n > 0:
        if n % 10 > maxi:
            maxi = n % 10
        n = n // 10
    print(maxi)
func4()
        ##   Задание 5   ###
def func5():
    profit = int(input('Введите прибыль'))
    costs = int(input('Введите расходы'))
    x = profit - costs
    if x > 0:
        a = profit / x
        c = int(input('Введите количество сотрудников'))
        c = x / c
        print(f'Вы работаете в плюс. Прибыль составила {x}р., рентабельность выручки приблизительно:{int(a)},прибыль на сотрудника{c}р.')
    elif x == 0:
        print(f'Вы работаете в ноль. Прибыль составила {x}р.')
    else:
        print(f'Вы работаете в минус. Убыток составил {x*-1}р.')
func5()
        ##   Задание 6   ###
def func6(a, b):
    c = 0
    s = 0
    while s <= b :
        s = a
        c += 1
        print(s,c)
        a = a + (a * 0.1)
    print(c)
func6(2, 3)
