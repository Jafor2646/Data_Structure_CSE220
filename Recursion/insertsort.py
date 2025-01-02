def insertSort(arr, low, high):
    if low >= high:
        return
    else:
        insertSort(arr, low, high-1)
        key = arr[high]
        j = high-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
x = [7, 4, 6, 5, 9, 3, 8, 12, 10]
insertSort(x, 0, len(x)-1)
print(x)