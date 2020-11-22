from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        a = ''
        for i in self.list_of_lists:
            a += f'{i}\n'
        return a

    def __add__(self, other):
        num_str = len(self.list_of_lists)
        num_col = len(other.list_of_lists[0])
        for i in range(num_str):
            for j in range(num_col):
                self.list_of_lists[i][j] = self.list_of_lists[i][j] + other.list_of_lists[i][j]
            result = self.list_of_lists
        return Matrix(result)


matrix = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
matrix1 = Matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(matrix)
print(matrix + matrix1)


class Clothes(ABC):
    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    def cloth(self):
        a = self.v / 6.5 + 0.5
        return a


class Suit(Clothes):
    def __init__(self, h):
        self.h = h
    @property
    def cloth(self):
        a = 2 * self.h + 0.3
        return a


c = Coat(20)
s = Suit(20)
print(c.cloth())
print(s.cloth)


class Cell:
    def __init__(self, count_c):
        self.count_c = count_c

    def __str__(self):
        return f"Клетка. Количество ячеек: {self.count_c}"

    def make_order(self, cifr):
        a = ''
        for i in range(self.count_c):
            a += '*'
            if (i + 1) % cifr == 0:
                a += '\n'
        return a

    def __add__(self, other):
        result = self.count_c + other.count_c
        return Cell(result)

    def __sub__(self, other):
        if self.count_c - other.count_c >= 0:
            result = self.count_c - other.count_c
            return Cell(result)
        else:
            print('разность количества ячеек двух клеток меньше нуля')

    def __mul__(self, other):
        result = self.count_c * other.count_c
        return Cell(result)

    def __truediv__(self, other):
        result = self.count_c / other.count_c
        result = round(result)
        return Cell(result)


c = Cell(20)
c1 = Cell(2)
print(c + c1)
print(c - c1)
print(c * c1)
print(c / c1)
print(c.make_order(5))

