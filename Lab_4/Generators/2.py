class Gen:
    def __init__(self, n) -> None:
        self.n = n
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        x=self.x
        self.x += 2
        if x <= self.n:
            return x
        raise StopIteration


if __name__ == "__main__":
    print(*Gen(int(input())), sep=', ')