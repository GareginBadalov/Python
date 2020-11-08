def func1(n1=int(input('Введите число')), n2=int(input('Введите число'))):


    if n2==0:
        print('На ноль делить нельзя, запустите функцию еще раз')
    else:
        return n1/n2


print(func1())


def func2(**data):
    string=''
    for key, value in data.items():
        string+=value
        string+=', '
    return string


print(func2(Name='Sasha', Age='21', city='Moscow', phonenumber='+70000000000'  ))


def func3(n1, n2, n3):
    l = [n1, n2, n3]
    a = l.pop(l.index(max(l)))
    b = l.pop(l.index(max(l)))
    return a+b


print(func3(1,250,0))


def func4(x=float(input('Введите дробь')), y=int(input('Введите целое чило'))):
    print(x**y)
    a=x
    b=0
    for i in range(0,y-1,1):
        x*=a
    return x


print(func4())


def func5():
    n = input('ddd:')
    l1 = n.split(sep=' ')
    s = 0
    for i in l1:
        i = int(i)
        s += i
    print(s)
    n = input('ddd:')
    l2 = n.split(sep=' ')
    if 'e' in n:

        a = l2.index('e')
        l2 = l2[0:a:1]
        for i in l2:
            i = int(i)
            s += i
    else:
        for i in l2:
            i = int(i)
            s += i


    return s


print(func5())


def func6(s):
    s=s.capitalize()
    return s

print(func6('сегодня'))
def func6_1(s1):
    s1=s1.split()
    b=''
    for i in s1:
        a=func6(i)
        b+=a
        b+=" "
    return b


print(func6_1('сегодня хороший день!'))
