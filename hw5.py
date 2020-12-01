import re
import json


def func1(*args):
    with open('func1.txt', 'w') as f_o:
        f_o.writelines(args)


func1('first string\n', 'second string\n', 'third string\n')


def func2():
    with open('func2.txt', 'r') as f_o:
        content = f_o.readlines()
        print(len(content))
        a=[]
        for i in content:
            i = i.split()
            a.append(len(i))
        print(a)

func2()


def func3():
    with open('func3.txt', 'r') as f_o:
        content = f_o.readlines()
        b = []
        a = 0
        c = 0
        for i in content[1::2]:
            if int(i) < 20000:
                b.append(content[content.index(i)-1][:-2])
            a += int(i)
            c += 1
        print(b)
        print(a/c)


func3()


def func4():
    with open('func4_1.txt', 'r') as f_o:
        content = f_o.readlines()
        a = []
        rus_c = ['Один - 1', 'Два - 2', 'Три - 3', 'Четыре - 4', 'Пять - 5',
               'Шесть - 6', 'Семь - 7', 'Восемь -8', 'Девять - 9', 'Десять - 10']
        for i in content:
            a.append(rus_c[content.index(i)])
            a.append('\n')
    with open('func4_2.txt', 'w', encoding='utf-8') as f_o1:
        f_o1.writelines(a)


func4()


def func5():
    with open('func5.txt', 'w') as f_o:
        f_o.write('1, 2, 3, 4, 5, 6, 7, 8')
    with open('func5.txt', 'r') as f_o:
        content = f_o.read()
        a = 0
        for i in content:
            try:
                a += int(i)
            except ValueError:
                continue
        print(a)


func5()


def func6():
    with open('func6.txt', 'r', encoding='utf-8') as f_o:
        content = f_o.readlines()
        my_dict = {}
        for i in content:
            result = re.findall(r'\d+', i)
            for j in result:
                result[result.index(j)] = int(j)
            my_sum = sum(result)
            i = i.split(': ')
            my_dict.update({i[0]: my_sum})
        print(my_dict)


func6()


def func7():
    with open('func7.txt', 'r', encoding='utf-8') as f_o:
        content = f_o.readlines()
        profit = []
        a = 0
        c = 0
        my_dict = {}
        for i in content:
            result = re.findall(r'\d+', i)
            profit.append(int(result[1]) - int(result[int(2)]))
        for j in profit:
            if j >= 0:
                a += j
                c += 1
                av_profit = a / c
        for i in content:
            z = i.split()
            my_dict.update({z[0]: profit[content.index(i)]})
        itog = [my_dict, {'average_profit': av_profit}]
    with open('func7_1.json', 'w', encoding='utf-8') as f_o1:
        json.dump(itog, f_o1)


func7()

