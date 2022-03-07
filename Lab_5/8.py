import re

pattern = r"[A-Z]+"
for i in ("ag,b,b.b", "aa, a.SD ASb", "ad,db, ads Sb jA"):
    print(i, ":", re.split(pattern, i))