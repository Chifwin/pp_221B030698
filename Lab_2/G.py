com = {}

for i in range(int(input())):
    s = input().split()
    if s[1] not in com:
        com[s[1]] = 1
    else:
        com[s[1]] += 1
        
for i in range(int(input())):
    s = input().split()
    if s[1] in com:
        com[s[1]] -= int(s[2])
        
print("Demons left:", sum((i for i in com.values() if i > 0)))
