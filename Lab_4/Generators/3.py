class Gen:
    def __init__(self, n) -> None:
        self.n = n
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        x = self.x
        self.x += 1
        while self.x%3 and self.x%4:
            self.x +=1
        if x <= self.n:
            return x
        raise StopIteration


def gen_func(n):
    for i in Gen(n): yield i

if __name__ == "__main__":
    for i in gen_func(int(input())):
        print(i)