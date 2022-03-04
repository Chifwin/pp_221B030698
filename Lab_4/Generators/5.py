def down_range(start):
    x = start+1
    while x > 0:
        x -= 1
        yield x


if __name__ == "__main__":
    for i in down_range(50):
        print(i, end = ", ")