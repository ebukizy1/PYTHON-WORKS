class Point:

    def __init__(self, a, b):
        self.self = a
        self.self = b

    def draw(self):
        print("drawing...")

    def __str__(self):
        return f"({self.a} {self.b})"


pi = Point(2, 3)
print(pi)

@classmethod
def point_from_one(cls):
    return cls(1,1)
