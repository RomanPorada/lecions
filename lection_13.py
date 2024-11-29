from math import pi

class Circle:
    pass

c1 = Circle()

print(type(c1))

c2 = object.__new__(Circle)

print(type(c2))

print(c1 == c2)
print(type(c1) == type(c2))

class Point:
    cls_var = 0

    def __new__(cls, x, y):
        print(f"Hello from the __new__ method")
        obj = object.__new__(cls)
        return obj
    
    def __init__(self, x, y):
        print(f"Hello from the __init__ method")
        self.x = x
        self.y = y

p1 = object.__new__(Point)
print(p1.__dict__)
print(type(p1))

p1.__init__(11, 22)
print(p1.__dict__)

p2 = Point(10, 9)

p3 = Point(18, 2006)

class Point2:
    def __new__(cls, x, y):
        print(f"Hello from the __new__ method")
        obj = object.__new__(cls)
        obj.x = x
        obj.y = y
        return obj

p2_1 = Point2(33, 44)
print(p2_1.__dict__)

class Point3:
    def __new__(cls, x, y):
        print(f"Hello from the __new__ method")
        obj = object.__new__(cls)
        return obj
    
    def __init__(self, x, y):
        print(f"Hello from the __init__ method")
        self.x = x
        self.y = y
    
    @staticmethod
    def say_hello():
        print("hello say_hallo method")

    @classmethod
    def create_point(cls, x, y):
        return cls(x, y)

p10 = Point3(55, 66)

p10.say_hello()

Point3.say_hello()

p11 = Point3.create_point(32, 43)
print(p11.__dict__)

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.area = self.get_area()

    def get_area(self):
        return pi * self.radius ** 2

    def __lt__(self, other):
        self.area < other.area

c1 = Circle(4, 3, 14)
c2 = Circle(2, 4, 2)
print(c1.get_area())   

print(Circle.get_area(c1))

print(c1.get_area() > c2.get_area())

print(c1< c2)