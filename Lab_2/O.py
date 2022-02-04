num = {"ONE":1, "TWO":2, "THR":3, "FOU":4, "FIV":5,
       "SIX":6, "SEV":7, "EIG":8, "NIN":9, "ZER":0}
st = {v: k for k,v in num.items()}

def to_num(x):
    if len(x) == 3:
        return num[x]
    return num[x[-3:]] + 10*to_num(x[:-3])

def to_st(x):
    if x < 10:
        return st[x]
    return to_st(x//10) + st[x%10]

print(to_st(sum(map(to_num, input().split("+")))))
