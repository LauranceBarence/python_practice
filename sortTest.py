def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)
    return arr


def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if i != min_index:
            arr[min_index], arr[i] = arr[i], arr[min_index]
        print(arr)
    return arr


def quick_sort(arr):
    if not arr:
        return []
    else:
        first = arr[0]
        left = quick_sort([l for l in arr[1:] if l < first])
        right = quick_sort([r for r in arr[1:] if r >= first])
        return left + [first] + right


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    print(arr)
    return arr


arr1 = [3, 5, 2, 1, 4, 7]

# bubble_sort(arr1)

# select_sort(arr1)

# print(quick_sort(arr1))

# insert_sort(arr1)
