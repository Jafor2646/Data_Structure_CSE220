inp = input()
arr = [None]*2
check = ""
count = 0
for i in range(len(inp)):
    if(ord('0') <= ord(inp[i]) and ord('9') >= ord(inp[i])):
        check += inp[i]
    else:
        arr[count] = int(check)
        count += 1
        check = ""
arr[count] = int(check)
n = arr[0]
m = arr[1]
arr1 = [None]*n
arr2 = [None]*m
inp = input()
check = ""
count = 0
for i in range(len(inp)):
    if(ord('0') <= ord(inp[i]) and ord('9') >= ord(inp[i])):
        check += inp[i]
    else:
        arr1[count] = int(check)
        count += 1
        check = ""
arr1[count] = int(check)
inp = input()
check = ""
count = 0
for i in range(len(inp)):
    if(ord('0') <= ord(inp[i]) and ord('9') >= ord(inp[i])):
        check += inp[i]
    else:
        arr2[count] = int(check)
        count += 1
        check = ""
arr2[count] = int(check)
sum = [None]*(m+n)
count = 0
for i in range(n):
    if arr1[i] not in sum:
        sum[i] = arr1[i]
        count += 1
for i in range(m):
    if arr2[i] not in sum:
        sum[n+i] = arr2[i]
        count += 1
print(arr1)
print(arr2)
print(sum)
print(count)
#1 23 2 435 2 6 67 44 99 1234
#32 43 2 6 7 45 54 44 88 3453 342 2345