ar = map(int, input().split())
cur = 0
res = True
for i in ar:
    cur = max(cur-1, i)
    if cur <= 0:
        res = False
        break
if res:
    print(1)
else:
    print(0)
