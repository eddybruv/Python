def remove_stuff(arr):
    first = arr[0]
    second = arr[4]
    third = arr[5]
    arr.remove(first)
    arr.remove(second)
    arr.remove(third)



a_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

remove_stuff(a_list)
print(a_list)