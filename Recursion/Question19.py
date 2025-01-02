def changeXY(s):
    if s == '':
        return ''
    if s[0] == 'x':
        return 'y' + changeXY(s[1:])
    return s[0] + changeXY(s[1:])
print(changeXY("codex"))
print(changeXY("xxhixx"))
print(changeXY("xhixhix"))