import re

def reg(s):
    return re.match(r"ab{2,3}", s)

for i in ("gbbb", "a ab abbb abbbs", "abbbb"):
    res = reg(i)
    print(i, ":", res[0] if res else "Not founded")