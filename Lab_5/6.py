import re

pattern = r"[., ]"
for i in ("ag,b,b.b", "aa, a.SD ASb", "ad,db, ads Sb jA"):
    print(i, ":", re.sub(pattern, ':', i))