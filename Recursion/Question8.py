def countAbc(s):
    if len(s) <= 2:
        return 0
    if s[0] == 'a' and s[1] == 'b' and (s[2] == 'c' or s[2] == 'a'):
        return 1 + countAbc(s[3:])
    else:
        return countAbc(s[1:])
print(countAbc("abc"))
print(countAbc("abcxxabc"))
print(countAbc("abaxxaba"))