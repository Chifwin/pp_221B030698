import re

pattern = r"ab{2,3}"
for i in ("gbbb", "a ab abbb abbbs", "abbbb"):
    res = re.match(pattern, i)
    print(i, ":", res[0] if res else "Not founded")