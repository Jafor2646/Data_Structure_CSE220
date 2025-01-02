def find_closing_parenthesis(s, i):
#         if s[i] == ')':
#             return i
#         elif i == len(s) - 1:
#             return -1
#         else:
#             return find_closing_parenthesis(s,i + 1)

# def parenBit(s):
#     start_index = s.find('(')
#     if start_index == -1:
#         return ''
#     end_index = find_closing_parenthesis(s, start_index + 1)
#     if end_index == -1:
#         return ''
#     return s[start_index:end_index+1]