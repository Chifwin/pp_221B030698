import re

pattern = r"(?<=_)([a-z])"
for i in ("agbbb_de", "aaahy_ahb", "addb_awer_fr_g54"):
    new = "".join(x.title() for x in i.split("_"))
    print(new)