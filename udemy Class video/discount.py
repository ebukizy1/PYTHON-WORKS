import unittest


class MyClass:
    def __init__(self, price, discount):
        self.__price = price
        self.__discount = discount

    def disCount_Price(self):
        if self.__price < 0 or self.__discount < 0:
            raise TypeError
        if type == int:
                raise TypeError
        value = self.__price // self.__discount
        return value

