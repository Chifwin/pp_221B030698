import re

def reg(s):
    return re.findall(r"[A-Z][a-z]+", s)

for i in ("Agbbb", "aaaSD ASf", "Addd adsSd jA"):
    print(i, ":", ", ".join(reg(i)))