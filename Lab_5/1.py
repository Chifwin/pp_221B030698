import re

pattern = r"ab*"
for i in ("gbbb", "a ab abbb abbbs", "abbb abbbs"):
    res = re.match(pattern, i)
    print(i, ":", res[0] if res else "Not founded")