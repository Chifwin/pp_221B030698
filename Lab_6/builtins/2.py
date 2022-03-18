def func(x: str):
    return (sum((i.islower() for i in x)), sum((i.isupper() for i in x)))


if __name__ == "__main__":
    for i in ("asdfg", "ASDFG", "[7, 8,dFTw"):
        print(f"{i}:\t{func(i)}")