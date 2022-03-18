def func(x):
    return all(x)

if __name__ == "__main__":
    for i in (('1', "1254c"), (0, 1245), (True, False), (True,)):
        print(f"{i}:\t{func(i)}")