from pkgutil import ImpImporter
from _2 import Shape

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def area(self):
        return self.__lenght * self.__width

if __name__ == "__main__":
    rec = Rectangle(1, 5)
    print(f"res area = {rec.area()}")
    print(f"Rectangle(5, 10) area = {Rectangle(5, 10).area()}")