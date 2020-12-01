import datetime
from time import sleep


class TrafficLight:
    def __init__(self, color):
        self._color = color

    def running(self):
        for i in range(2):
            print(self._color)
            sl1 = datetime.datetime.now()
            sleep(7)
            sl2 = datetime.datetime.now()
            delta = sl2 - sl1
            if delta.seconds != 7:
                raise RuntimeError('Светофор работает неправильно')
            self._color = 'yellow'
            print(self._color)
            sl1 = datetime.datetime.now()
            sleep(2)
            sl2 = datetime.datetime.now()
            delta = sl2 - sl1
            if delta.seconds != 2:
                raise RuntimeError('Светофор работает неправильно')
            self._color = 'green'
            print(self._color)
            sl1 = datetime.datetime.now()
            sleep(5)
            sl2 = datetime.datetime.now()
            delta = sl2 - sl1
            if delta.seconds != 5:
                raise RuntimeError('Светофор работает неправильно')
            self._color = 'red'


def traffic_light_run(color):
    traffic_light01 = TrafficLight(color)
    traffic_light01.running()


traffic_light_run('red')


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt(self, masph, thickn):
        a = self.__length * self.__width * masph * thickn
        print(f"Для покрытия асфальтом {self.__length * self.__width}кв.м дороги потребуется {a//1000}т. асфальта")


def asphal(len_r, w, m, t):
    road1 = Road(len_r, w)
    road1.asphalt(m, t)


asphal(5000, 20, 25, 5)


wage_dict = {"driverw": 30000, "driverb": 10000, "managerw": 40000, "managerb": 20000}


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_income(self):
        return self.__income


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name}  {self.surname} ")

    def get_total_income(self):
        a = self.get_income()
        print(f"Total income: {self.get_income()[self.position + 'w'] + self.get_income()[self.position + 'b']}")


driver = Position('Vasiliy', 'Ivanov', 'driver', wage_dict)
manager = Position('Ivan', 'Petrov', 'manager', wage_dict)
driver.get_full_name()
driver.get_total_income()
manager.get_full_name()
manager.get_total_income()


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car in motion at a speed of  {self.speed} km\h')

    def stop(self):
        print('car stopped')

    def turn_direction(self, direction):
        if direction == 'left':
            print('car turned left')
        else:
            print('car turned right')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed}! OverSpeed!')



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed}! OverSpeed!')
    pass


class PoliceCar(Car):
    pass


bmw = TownCar(62, 'Yellow', '3 series')
bugatti = SportCar(60, 'Blue', 'Chiron')
freightliner = WorkCar(41, 'Orange', 'Cascadia')
ford = PoliceCar(70, 'White', 'Crown Victoria')
bmw.show_speed()
freightliner.show_speed()
ford.show_speed()
bugatti.go()
bugatti.stop()
bugatti.turn_direction('left')


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
    pass


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
    pass


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')
    pass


st = Stationery('родитель')
st.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
