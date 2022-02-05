a = []
def is_strong_pass(s):
    upper = lower = num = False
    for i in s:
        if i.isdigit():
            num = True
        elif i.isupper():
            upper = True
        elif i.islower():
            lower = True
    return num and lower and upper
    
for i in range(int(input())):
    c = input()
    if is_strong_pass(c) and c not in a:
        a.append(c)

print(len(a), *sorted(a), sep="\n")
