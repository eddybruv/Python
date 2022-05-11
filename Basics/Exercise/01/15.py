def swap(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp


a_list = [1, 2, 4, 5, 6, 7, 9, 0]
swap(a_list)

print(a_list)
