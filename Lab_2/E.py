n, x = map(int, input().split())
arr = [x+2*i for i in range(n)]
res = 0
for i in arr:
    res ^= i
print(res)
