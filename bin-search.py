def bin_search(lst, x):
    # O(log2 n)
    lower_bound = 0
    upper_bound = len(lst)
    while lower_bound != upper_bound:
        compared_value = (lower_bound + upper_bound) // 2
        if x == lst[compared_value]:
            return x
        elif x < lst[compared_value]:
            upper_bound = compared_value
        else:
            lower_bound = compared_value + 1
    return None

if __name__ == "__main__":
    lst = [int(x) for x in input('Enter the array: ').split()]
    print(lst)
    x = int(input('Enter the element that you\'re trying to find: '))
    print(bin_search(lst, x))
