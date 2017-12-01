def bubble_sort(lst):
    # O(n ^ 2)
    for _ in range(len(lst) - 1):
        for i in range(1, len(lst) - 1):
            if lst[i - 1] > lst[i]:
                tmp = lst[i - 1]
                lst[i - 1] = lst[i]
                lst[i] = tmp
    return lst

if __name__ == "__main__":
    arr = [1, -4, 5, 3, 6, 23, 45, -23, 14]
    print(bubble_sort(arr))
