def remove_dup(arr):
    return list(dict.fromkeys(arr))

a_list = [1, 2, 1, 1, 1, 2, 3, 4, 3, 6, 4, 3, 6, 7]
arr = remove_dup(a_list)

print(arr)