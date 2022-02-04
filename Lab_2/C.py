n = int(input())
for i in range(n):
    for j in range(n):
        if i == j:
            print(i*j, end=" ")
        elif i*j == 0:
            print(i if i else j, end=" ")
        else:
            print(0, end=" ")
    print()
