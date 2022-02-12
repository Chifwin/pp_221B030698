from itertools import permutations

def print_all_prem(s: str):
    for i in permutations(s):
        print(*i, sep="")

if __name__ == "__main__":
    s = input("String is: ")
    print(f"Permitations of string {s}:")
    print_all_prem(s)
