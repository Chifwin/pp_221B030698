for _ in range(int(input())):
    s = input()
    if len(s) > 10 and s[-10:] == "@gmail.com":
        print(s[:-10])