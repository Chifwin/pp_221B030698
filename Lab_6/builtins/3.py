def func(x: str):
    return x == x[::-1]


if __name__ == "__main__":
    for i in ("asa", "asA", "asdfgh"):
        print(f"{i}:\t{func(i)}")