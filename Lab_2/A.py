ar = list(map(int, input().split()))
cur = 0
res = True
for ind, i in enumerate(ar):
    cur = max(cur-1, i)
    if cur <= 0:
        if ind != len(ar)-1:
            res = False
        break
if res:
    print(1)
else:
    print(0)
