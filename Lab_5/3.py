import re

pattern = r"[a-z]+_"
for i in ("gbbb_", "a_ aaSD ASD_", "Addd adsSd_ j_"):
    res = re.findall(pattern, i)
    print(i, ":", res)