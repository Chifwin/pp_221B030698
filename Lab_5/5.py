import re

pattern = r"a[.|\D]*b"
for i in ("agbbb", "aaaSD ASb", "addb adsSb jA"):
    res = re.findall(pattern, i)
    print(i, ":", res)