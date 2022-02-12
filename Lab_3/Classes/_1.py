class IO:
    def __init__(self):
        self.__s = ''
    
    def getString(self):
        self.__s = input()

    def printString(self):
        print(self.__s)


if __name__ == "__main__":
    obj = IO()
    obj.getString()
    obj.printString()
    obj.printString()
    obj.getString()
    obj.printString()