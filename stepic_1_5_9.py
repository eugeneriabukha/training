# -*- coding: utf-8 -*-
__author__ = 'eugene.riabukha'


class Buffer:
    def __init__(self):
        # конструктор без аргументов
        pass

    def add(self, *a):
        # добавить следующую часть последовательности
        if hasattr(self, "buff"):
            self.buff.extend(list(a))
        else:
            self.buff = list(a)
        if self.buff.__len__()//5 != 0:
            for i in range(self.buff.__len__()//5):
                print(sum(self.buff[i*5:(i+1)*5]))

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        if hasattr(self, "buff"):
            self.buff = self.buff[(self.buff.__len__()//5)*5:]
            return self.buff

if __name__ == "__main__":
    buf = Buffer()
    buf.add(1, 2, 3)
    buf.get_current_part() # вернуть [1, 2, 3]
    buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
    buf.get_current_part() # вернуть [6]
    buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
    buf.get_current_part() # вернуть []
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
    buf.get_current_part() # вернуть [1]
