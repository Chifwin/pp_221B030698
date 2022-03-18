from time import sleep
from math import sqrt


def func(x, sec):
    sleep(sec/1000)
    return sqrt(x)

if __name__ == "__main__":
    for i in ((1, 2), (50, 1245), (1224, 4521)):
        print(f"{i}:\t{func(*i)}")