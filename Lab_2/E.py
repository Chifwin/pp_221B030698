s = input().split()
if len(s) == 2:
    n, x = map(int, s)
else:
    n = int(s[0])
    x = int(input())
arr = [x+2*i for i in range(n)]
res = 0
for i in arr:
    res ^= i
print(res)
