def strCount(s, sub):
    if len(s) < len(sub):
        return 0
    if s[:len(sub)] == sub:
        return 1 + strCount(s[len(sub):], sub)
    return strCount(s[1:], sub)
print(strCount("catcowcat", "cat"))
print(strCount("catcowcat", "cow"))
print(strCount("catcowcat", "dog"))