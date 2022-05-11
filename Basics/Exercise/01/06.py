def second(arr):
    return arr[1]


def sort_fxn(arr):
    return arr.sort(key=second)


a_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sort_fxn(a_list)
print(a_list)
