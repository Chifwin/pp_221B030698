a = []
for i in range(int(input())):
    c = input().split()
    if c[0] == "1":
        a.append(c[1])
    else:
        print(a.pop(0), end=" ")

