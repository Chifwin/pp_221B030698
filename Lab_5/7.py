import re

def ToCamelCase(s):
    return "".join((x.title() for x in s.split("_")))

for i in ("agbbb_de", "aaahy_ahb", "addb_awer_fr_g54", "i_love_python"):
    print(f"{i}:\t{ToCamelCase(i)}")