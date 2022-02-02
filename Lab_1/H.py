s = input()
t = input()

if t in s:
    a, b = s.find(t), s.rfind(t)
    print(a, (b if a != b else ""))