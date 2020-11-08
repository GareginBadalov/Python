
def func1(*elem):
    a=[*elem]
    typelist = []
    for i in a:
        b = type(i)
        typelist.append(b)
    print(typelist)
func1(1, 2, True, False, (1, 2), 'string', 1.0)

def func2():
    n = input('Введите значения списка, через запятую  ",":').split(',')
    a=0
    print(n)
    for i in n:
        print(a)
        if n.index(i)%2==0:
            a = n.index(i)
            continue
        else:
            b=n.index(i)
            b=int(b)
            n[a], n[b] = n[b], n[a]
    print(n)
func2()
def func3():
    n=int(input("Введите номер месяца"))
    list1=[(1,2,12),(3,4,5),(6,7,8),(9,10,11)]
    a=0
    for i in list:
        if n in list[1]:
            print('spring')
            break
        elif n in list[0]:
            print('winter')
            break
        elif n in list[2]:
            print('Summer')
            break
        elif n in list[1]:
            print('Autumn')
            break

func3()


def func3_1():
    n = int(input("Введите номер месяца"))
    w = {12: 'Winter', 3: "Spring", 1: 'Winter', 2: 'Winter', 4: "Spring", 5: "Spring", 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}
    print(w[n])
func3_1()


def func4():
    n=input("Enter string")
    ts=n.split()
    for i in ts:
        if len(i)>=10:
            print((ts.index(i)+1), i[0:10:])
        else:
            print((ts.index(i)+1), i)

func4()


def func5():
    list1 = [7, 5, 3, 3, 2]
    n = int(input('Введите число'))
    c = 0
    for i in list1:
        if n < i:
            c += 1
    list1.insert(c, n)
    print(list1)
func5()

def func6():
    title = input('Введите название')
    price = input('Введите цену')
    tcount = input('Введите количество')
    ed = input('Введите единицу измерения')                                                                             #ввод значений нового товара
    goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
    ]                                                                                                                   #Исходный список товаров
    new_product = ((goods[-1][0]+1), {'название': title, 'цена': price, 'количество': tcount, 'eд': ed})
    goods.append(new_product)                                                                                           #сбор данных от пользователя в один объект и добавление в исходный список
    k = goods[0][1].keys()
    k = list(k)
    a = 0
    b = a + 1
    titles = {}
    prices = {}
    tcounts = {}
    eds = {}
    analysis = {}
    while a != len(goods):                                                                                              #добавление элементов в новый словарь
        titles.setdefault((k[0]), []).append(goods[a][b][(k[0])])
        prices.setdefault((k[1]), []).append(goods[a][b][(k[1])])
        tcounts.setdefault((k[2]), []).append(goods[a][b][(k[2])])
        eds.setdefault((k[3]), []).append(goods[a][b][(k[3])])
        a += 1
    analysis.update(titles)
    analysis.update(prices)
    analysis.update(tcounts)
    analysis.update(eds)
    print(analysis)
#Возможно где-то можно было поступить проще, в этом плане опыта не хватает.


func6()








