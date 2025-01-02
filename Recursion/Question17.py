def store(s):
    if s[0] == ')':
        return s[0]
    return s[0] + store(s[1:])
def parenBit(s):
    if s[0] == '(':
        temp = store(s)
        return temp
    return parenBit(s[1:])

def findClosingParenthesis(s, i, si):
        if s[i] == ')':
            return i
        elif i == si:
            return -1
        else:
            return findClosingParenthesis(s,i - 1, si)

def parenBit(s):
    start_index = s.find('(')
    if start_index == -1:
        return ''
    end_index = findClosingParenthesis(s, len(s)-1, start_index)
    if end_index == -1:
        return ''
    return s[start_index:end_index+1]


print(parenBit("x(y(z(abc)1)2)3"))
print(parenBit("x(hello)"))
print(parenBit("xy1"))

