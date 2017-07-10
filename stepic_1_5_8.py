__author__ = 'eugene.riabukha'


class MoneyBox:
    def __init__(self, capacity):
        # ����������� � ���������� � ����������� �������
        self.capacity = capacity
        self.kol = 0

    def can_add(self, v):
        # True, ���� ����� �������� v �����, False �����
        return self.kol + v <= self.capacity

    def add(self, v):
        # �������� v ����� � �������
        if self.can_add(v):
            self.kol += v
