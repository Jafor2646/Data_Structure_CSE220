def noX(s):
    if s == "":
        return s
    if s[0] == 'x':
        return noX(s[1:])
    return s[0] + noX(s[1:])
print(noX("xaxb"))
print(noX("abc"))
print(noX("xx"))