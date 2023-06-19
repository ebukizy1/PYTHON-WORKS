from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal, age: int):
        self.name = name
        self.balance = balance
        self.age = age

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("balance cannot be negative")
        self.__balance = amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("you want to scam us")
        self.__balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("you want to scam us")
        self.__balance += amount

    def __str__(self):
        return f"{self.name} {self.balance} {self.age}"


account1 = Account("emmanuel", Decimal(100.00), 30)
print(account1)
