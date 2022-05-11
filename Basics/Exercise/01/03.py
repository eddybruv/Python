def get_largest(arr):
    max = arr[0]
    for x in arr:
        if x > max:
            max = x
    return max


a_list = [1, 4, 5, 7, 8, 3, 2, 6, 8, 0, 9, 2, 3, 5, 7, 8]

print(get_largest(a_list))