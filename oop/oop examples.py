class Human():
    numbers_of_eyes = 2
    numbers_of_nose = 4

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hello {self.name}")


human1 = Human("esther")
print(human1.greet())





print(human1.numbers_of_eyes)
print(human1.numbers_of_nose)
