s = input()
res = 0
for i in s:
    res += ord(i)
if res > 300:
    print("It is tasty!")
else:
    print("Oh, no!")