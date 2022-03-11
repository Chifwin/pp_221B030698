import re

def reg(s):
    return re.split(r"[A-Z]+", s)

for i in ("ag,b,b.b", "aa, a.SD ASb", "ad,db, ads Sb jA"):
    print(i, ":", ", ".join(reg(i)))