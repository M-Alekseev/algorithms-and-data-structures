def quick_sort(arr):
    # O(n * log n)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# testing
lst = [1, 3, 2, 5, 12, 31, 23, -2, -1, -42]
print("Given array: \n" + str(lst))
print(quick_sort(lst))
