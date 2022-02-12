class Shape:
    def __init__(self):
        self.__area = 0
    
    def area(self):
        return self.__area

class Square(Shape):
    def __init__(self, lenght):
        self.__lenght = lenght

    def area(self):
        return self.__lenght ** 2

if __name__ == "__main__":
    shape = Shape()
    square = Square(5)
    print(f"shape area = {shape.area()}")
    print(f"square area = {square.area()}")