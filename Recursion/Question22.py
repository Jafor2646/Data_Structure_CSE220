def countPairs(s):
    if len(s) <= 2:
        return 0
    if s[0] == s[2]:
        return 1 + countPairs(s[1:])
    return countPairs(s[1:])
print(countPairs("axa"))
print(countPairs("axax"))
print(countPairs("axbx"))