def strDist(s, sub):
    if len(s) < len(sub):
        return 0
    if s[:len(sub)] != sub:
        return strDist(s[1:],sub)
    lastIndex = s.rfind(sub)
    return len(sub)+lastIndex


print(strDist("catcowcat", "cat"))
print(strDist("catcowcat", "cow"))
print(strDist("cccatcowcatxx", "cat"))