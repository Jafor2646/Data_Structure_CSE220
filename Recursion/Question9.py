def countHi2(s):
    if len(s) <= 1:
        return 0
    if s[0] == 'x':
        return countHi2(s[3:])
    if s[0] == 'h' and s[1] == 'i':
        return 1 + countHi2(s[2:])
    return countHi2(s[1:])
print(countHi2("ahixhi"))
print(countHi2("ahibhi"))
print(countHi2("xhixhi"))