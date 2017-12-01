def find_peak(lst):
    mid = len(lst) // 2
    if mid == 0 or lst[mid - 1] <= lst[mid] and mid == len(lst) - 1 or lst[mid + 1] <= lst[mid]:
        return lst[mid]
    elif mid > 0 and lst[mid + 1] < lst[mid]:
        return find_peak(lst[:mid])
    else:
        return find_peak(lst[mid + 1:])


if __name__ == "__main__":
    array = [3, 0, 2, 1, 5, 9, 6, 7, 4]
    array.sort()
    result = find_peak(array)
    print("Peak element is: {}".format(result))
