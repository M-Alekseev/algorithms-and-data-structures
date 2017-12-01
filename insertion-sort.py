def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while lst[j - 1] > lst[j] and j > 0:
            tmp = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = tmp
            j -= 1
    return lst

if __name__ == "__main__":
    arr = [2, 3, 1, 4, 8, 5, -15, -3, 26, 37, -19, -1]
    print(insertion_sort(arr))
