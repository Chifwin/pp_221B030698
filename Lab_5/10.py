import re

pattern = r"([a-z])([A-Z]+)"
for i in ("agbbbDe", "aaahyAhb", "addbAwerFr"):
    print(i, ":", re.sub(pattern, r"\1_\2", i).lower())