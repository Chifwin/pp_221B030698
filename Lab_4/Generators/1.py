def gen(N):
    return (i*i for i in range(N+1))

if __name__ == "__main__":
    for i in gen(50):
        print(i)