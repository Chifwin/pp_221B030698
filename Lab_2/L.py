a = []
res = True
for i in input():
    if i in "[{(":
        a.append(i)
    elif len(a) and (i == "}" and a[-1] == "{" or
                      i == "]" and a[-1] == "[" or
                      i == ")" and a[-1] == "("):
        a.pop()
    else:
        res = False
        break

print("Yes" if res and not len(a) else "No")
