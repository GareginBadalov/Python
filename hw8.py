from time import sleep


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract(cls, date):
        a = []
        for i in date.split('-'):
            a.append(int(i))
        return a

    @staticmethod
    def valid(date):
        a = []
        for i in date.split('-'):
            a.append(int(i))
        if a[0] not in range(1, 32):
            raise ValueError('В одном месяце максимум 31 день')
        elif a[1] not in range(1, 13):
            raise ValueError('В одном году 12 месяцев')
        else:
            return date

    def valid1(self):
        return Date.valid(self.date)


date1 = Date('12-12-2012')
print(Date.extract('12-12-2012'))
print(date1.valid1())


# Задание2
class MyError(Exception):
    def __init__(self, text):
        self.text = text


a = int(input('Введите делимое'))
b = int(input('Введите делитель'))

try:
    if b == 0:
        raise MyError('на ноль делить нельзя')
except MyError as error:
    print(error)
else:
    print(f'Результат: {a / b}')
finally:
    print('Программа завершена')


# Задание3
class MyError1(Exception):
    def __init__(self, text):
        self.text = text


error = MyError1('вы Ввели не число')
a = []
while True:
    try:
        n = input('Введите следующее значение')
        if n.lower() == 'stop':
            break
        if n.isdigit():
            a.append(n)
        else:
            raise error
    except MyError1:
        print(error)
print(a)


# Задание4
class Warehouse:
    a = {}
    count_p = 0
    count_s = 0
    count_x = 0

    def get(self, equip):
        if type(equip) == Printer:
            self.count_p += 1
            self.a.update({equip.name: equip.__str__(), "Количество принтеров": self.count_p})
        elif type(equip) == Scaner:
            self.count_s += 1
            self.a.update({equip.name: equip.__str__(), "Количество сканеров": self.count_s})
        else:
            self.count_x += 1
            self.a.update({equip.name: equip.__str__(), "Количество ксероксов": self.count_x})

    def send(self, equip, dep):

        if type(equip) == Printer:
            del self.a[equip.name]
            self.count_p -= 1
            self.a.update({"Количество принтеров": self.count_p})
        elif type(equip) == Scaner:
            del self.a[equip.name]
            self.count_s -= 1
            self.a.update({"Количество сканеров": self.count_s})
        else:
            del self.a[equip.name]
            self.count_x -= 1
            self.a.update({"Количество ксероксов": self.count_x})


class Office_eq:
    def __init__(self, name, speed, size, price):
        self.speed = speed
        self.size = size
        self.price = price
        self.name = name
        self.valid()

    @staticmethod
    def get_info(cls):
        print(f'Офисная техника. Пример класса {cls}')

    def valid(self):
        try:
            self.speed = int(self.speed)
            self.price = int(self.price)
        except ValueError:
            print('Скорость и цена должны быть числом. Создайте экземпляр заного')
            if type(self) == Printer:
                warehouse.count_p -= 1
            elif type(self) == Scaner:
                warehouse.count_s -= 1
            else:
                warehouse.count_x -= 1
            del self

    def turn_on(self):
        print('Working')

    def turn_off(self):
        print('stopped')

    def __str__(self):
        return f"{self.name}, Скорость работы: {self.speed}, " \
               f"Размер: {self.size} Цена:{self.price}"


class Printer(Office_eq):
    def work(self, file):
        self.turn_on()
        for i in file:
            print(f'Печать {i}-го листа завершена')
            sleep(1)


class Scaner(Office_eq):
    def work(self, file):
        self.turn_on()
        for i in file:
            print(f'Сканировонаие {i}-го листа завершено')
            sleep(1)


class Xerox(Office_eq):
    def work(self, file):
        self.turn_on()
        for i in file:
            print(f'Копирование {i}-го листа завершено')
            sleep(1)


printer = Printer('HP', 10, '25*45*13', 3800)
warehouse = Warehouse()

printer1 = Printer('Toshiba', 'as', '25*45*13', 5800)
printer2 = Printer('Samsung', 40, '25*45*13', 8800)
scaner = Scaner('Samsung', 12, '25*45*13', 1300)
scaner1 = Scaner('hp', 40, '25*45*13', 20000)
warehouse.get(printer)
warehouse.get(printer1)
warehouse.get(printer2)
warehouse.get(scaner)
warehouse.get(scaner1)
warehouse.send(scaner1, ' econom')
warehouse.send(scaner, ' econom')
print(warehouse.a)
printer.get_info(printer)


class Complex:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __add__(self, other):
        result = complex(self.a, self.b) + complex(other.a, other.b)
        return result

    def __mul__(self, other):
        result = complex(self.a, self.b) * complex(other.a, other.b)
        return result


cifr = Complex(2, 4)
cifr1 = Complex(3, 6)
print(cifr + cifr1)
print(cifr * cifr1)
