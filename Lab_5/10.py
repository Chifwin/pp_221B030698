import re

def to_snake_case(s):
    return re.sub(r"([a-z])([A-Z]+)", r"\1_\2", s).lower()

for i in ("agbbbDe", "aaahyAhb", "addbAwerFr", "iLovePython", "snakeCaseIsBetter"):
    print(i, ":", to_snake_case(i))