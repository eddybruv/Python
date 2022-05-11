def remove_even(arr):
    for x in arr:
        if x % 2 == 0:
            arr.remove(x)

a_list = [1, 2, 3, 4, 5, 7, 8, 6, 9, 10, 12, 11, 13, 14]

remove_even(a_list)

print(a_list)