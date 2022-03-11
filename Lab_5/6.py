import re

def reg(s):
    return re.sub(r"[., ]", ":", s)

for i in ("ag,b,b.b", "aa, a.SD ASb", "ad,db, ads Sb jA"):
    print(i, ":", reg(i))