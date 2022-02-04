n = int(input())
for i in range(n):
    for j in range(n):
        if n%2 and i+j >= n-1 or not n%2 and j <= i:
            print('#', end='')
        else:
            print(".", end='')
    print()
