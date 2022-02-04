com = {}
for i in range(int(input())):
    s = input().split()
    if s[0] not in com:
        com[s[0]] = int(s[1])
    else:
        com[s[0]] += int(s[1])
m = max(com.values())
for i in sorted(com.keys()):
    print(i, end=" ")
    if com[i] == m:
        print("is lucky")
    else:
        print(f"has to recieve {m - com[i]} tenge")
