def length(s):
    if s == "":
        return 0
    return 1+length(s[1:])
print(length("abcd"))