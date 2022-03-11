import re

def reg(s):
    return re.findall(r"[a-z]+_", s)

for i in ("gbbb_", "a_ aaSD ASD_", "Addd adsSd_ j_"):
    print(i, ":", ", ".join(reg(i)))