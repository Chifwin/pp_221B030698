def toLowercase(s):
    res = ""
    for i in s:
        if "A" <= i and i <= "Z":
            res += chr(ord(i) - ord("A") + ord("a"))
        else:
            res += i
    return res

print(toLowercase(input()))
