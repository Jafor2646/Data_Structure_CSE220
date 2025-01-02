def count11(s):
    if len(s) <= 1:
        return 0
    if s[0] == '1' and s[1] == '1':
        return 1 + count11(s[2:])
    return count11(s[1:])
print(count11("11abc11"))
print(count11("abc11x11x11"))
print(count11("111"))
    