import re

def reg(s):
    return re.match(r"ab*", s)

for i in ("gbbb", "a ab abbb abbbs", "abbb abbbs"):
    res = reg(i)
    print(i, ":", res[0] if res else "Not founded")