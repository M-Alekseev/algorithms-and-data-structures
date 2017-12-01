def merge_sort(lst):
    if len(lst) == 1:
        return lst

    result = []
    i = 0
    j = 0
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


if __name__ == "__main__":
    arr = [2, 3, 5, 1, 6, 8, 4]
    print(merge_sort(arr))
