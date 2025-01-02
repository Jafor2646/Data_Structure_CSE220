def chnagePi(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == 'p' and s[1] == 'i':
        st = '3.14'
        s = st + s[2:]
        return s[:4] + chnagePi(s[4:])
    else:
        return s[:1] + chnagePi(s[1:])
print(chnagePi("xpix"))
print(chnagePi("pipi"))
print(chnagePi("pip"))