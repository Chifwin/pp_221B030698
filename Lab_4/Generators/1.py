class Gen:
    def __init__(self, n) -> None:
        self.n = n
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        self.x += 1
        if self.x <= self.n:
            return self.x**2
        raise StopIteration


if __name__ == "__main__":
    a = Gen(5)
    iter(a)
    print(next(a))
    print(next(a))
    for i in Gen(10):
        print(i, end = ' ')