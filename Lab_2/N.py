a = []
s = input()
while s != "0":
    a.append(int(s))
    s = input()

for i in range(len(a)//2):
    print(a[i] + a[-i-1], end=" ")
    
if len(a)%2:
    print(a[len(a)//2])
