def countX(s):
    if s == "":
        return 0
    if s[0] == 'x':
        return 1 + countX(s[1:])
    else:
        return countX(s[1:])
print(countX("xxhixx"))
print(countX("xhixhix"))
print(countX("hi"))