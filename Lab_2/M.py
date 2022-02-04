a = []
while (s := input()) != "0":
    a.append(list(reversed(s.split())))

for i in sorted(a):
    print(" ".join(list(reversed(i))))
