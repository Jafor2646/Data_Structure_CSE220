def nestParen(s):
    if len(s) == 0:
        return True
    if s[0] == '(' and s[len(s)-1] == ')':
        return nestParen(s[1:len(s)-1])
    else:
        return False
print(nestParen("(())"))
print(nestParen("((()))"))
print(nestParen("(((x))"))
    