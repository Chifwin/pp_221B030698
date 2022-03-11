import re

def reg(s):
    return re.sub(r"([A-Z])", r" \1", s)

for i in ("agbbbDe", "aaahyAhb", "addbAwerFrG54"):
    print(i, ":", reg(i))