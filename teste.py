def partition(arr, left, right, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    store_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index


def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot = (right + left) // 2
    new_pivot_index = partition(arr, left, right, pivot)
    diff = new_pivot_index - left

    if diff == k:
        return arr[new_pivot_index]
    elif k < diff:
        return quickselect(arr, left, new_pivot_index - 1, k)
    else:
        return quickselect(arr, new_pivot_index + 1, right, k - diff - 1)


def median(arr):
    if not arr:
        return None

    length = len(arr)

    if length % 2 == 1:
        return quickselect(arr, 0, length - 1, length // 2)
    else:
        lower = quickselect(arr, 0, length - 1, length // 2 - 1)
        higher = quickselect(arr, 0, length - 1, length // 2)
        return (lower + higher) / 2.0


import random

array = [random.randint(0, 100) for _ in range(10)]
print(f"array ordenado: {sorted(array)}, mediana: {median(array)}")
