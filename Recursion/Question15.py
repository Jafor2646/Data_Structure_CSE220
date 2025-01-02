def endX(s):
    if len(s) == 0:
        return ''
    if s[0] == 'x':
        return endX(s[1:]) + 'x'
    return s[0] + endX(s[1:])
print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhix"))    