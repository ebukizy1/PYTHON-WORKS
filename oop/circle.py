import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area_of_a_radius(self):
       Area = math.pi * self.radius ** 2
       return f"the area of a radius is {Area}"

    def perimeter_of_circle(self):
        pi = 2 * math.pi * self.radius
        return f"the area of a radius is {pi}"


circle1 = Circle(10)
print(circle1.perimeter_of_circle())

print(circle1.area_of_a_radius())






