import re

def reg(s):
    return re.findall(r"a[.|\D]*b", s)

for i in ("agbbb", "aaaSD ASb", "addb adsSb jA"):
    print(i, ":", ", ".join(reg(i)))