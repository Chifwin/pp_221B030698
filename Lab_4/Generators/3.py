def gen(N):
    return (i for i in range(N+1) if i%3 == 0 or i%4 == 0)

if __name__ == "__main__":
    for i in gen(50):
        print(i)