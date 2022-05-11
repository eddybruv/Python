def get_smallest(arr):
    min = arr[0]
    for x in arr:
        if x < min:
            min = x
    return min


a_list = [1, 4, 5, 7, 8, 3, 2, 6, 8, 0, 9, 2, 3, 5, 7, 8]

print(get_smallest(a_list))
