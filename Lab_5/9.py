import re

pattern = r"([A-Z])"
for i in ("agbbbDe", "aaahyAhb", "addbAwerFrG54"):
    print(i, ":", re.sub(pattern, r" \1", i))