def strCopies(s, sub, n):
    if n == 0:
        return True
    if len(s) < len(sub):
        return False
    if s[:len(sub)] == sub:
        return  strCopies(s[len(sub):], sub, n-1)
    return strCopies(s[1:], sub, n)
print(strCopies("catcowcat", "cat", 2))
print(strCopies("catcowcat", "cow", 2))
print(strCopies("catcowcat", "cow", 1))
        
    