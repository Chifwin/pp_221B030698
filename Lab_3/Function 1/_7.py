def has_33(numbers: list):
    for  i in range(len(numbers)-1):
        if numbers[i] == 3 and numbers[i+1] == 3:
            return True
    return False

if __name__ == "__main__":
    print(f"has_33([1, 3, 3]) -> {has_33([1, 3, 3])}")
    print(f"has_33([1, 3, 1, 3]) -> {has_33([1, 3, 1, 3])}")
    print(f"has_33([3, 1, 3]) -> {has_33([3, 1, 3])}")
    s = list(map(int, input("Enter numbers: ").split()))
    print(f"has_33({s}) -> {has_33(s)}")
