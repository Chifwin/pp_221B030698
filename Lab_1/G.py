def to_dec(s):
    if len(s) == 0: return 0
    return int(s[-1]) + 2*to_dec(s[:-1])
    
print(to_dec(input()))