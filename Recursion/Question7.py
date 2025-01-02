def pairStar(s):
    if len(s) == 1 or len(s) == 0:
        return s
    if s[0] == s[1]:
        s = s[0] + '*' + s[1:]
        return s[:2] + pairStar(s[2:])
    return s[:1] + pairStar(s[1:])
print(pairStar("hello"))
print(pairStar("xxyy"))
print(pairStar("aaaa"))