def squares(start, stop):
    x = start-1
    while x < stop:
        x += 1
        yield x**2


if __name__ == "__main__":
    for i in squares(5, 50):
        print(i, end = ", ")