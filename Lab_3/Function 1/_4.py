def is_prime(x: int):
    if x%2 == 0: return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0: return False
    return True

def filter_prime(numbers: list):
    res = []
    for i in numbers:
        if is_prime(i):
            res.append(i)
    return res

if __name__ == "__main__":
    print("Prime numbers are: ", *filter_prime(list(map(int, input("List of numbers is: ").split()))))
