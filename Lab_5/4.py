import re

pattern = r"[A-Z][a-z]+"
for i in ("Agbbb", "aaaSD ASf", "Addd adsSd jA"):
    res = re.findall(pattern, i)
    print(i, ":", res)