def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp


a_list = [1, 2, 4, 5, 6, 7, 9, 0]
swap(a_list, pos1=3, pos2=1)

print(a_list)
