a = []
s = input()
while s != "0":
    a.append(list(reversed(s.split())))
    s = input()

for i in sorted(a):
    print(" ".join(list(reversed(i))))
