def is_prime(x):
    if x%2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x%i == 0:
            return False
    return True

n, f = map(int, input().split())
if n <= 500 and is_prime(n) and f%2 == 0:
    print("Good job!")
else:
    print("Try next time!")