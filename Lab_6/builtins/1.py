from math import prod

def func(x: list):
    return prod(x)


if __name__ == "__main__":
    for i in ([1, 2, 3, 4], [0, 2, 3], [7, 8, 99, 4]):
        print(f"{i}:\t{func(i)}")