a = []
for i in input().split():
    i = i.strip(",.!;?")
    if i not in a:
        a.append(i)
print(len(a), *(sorted(a)), sep="\n")
