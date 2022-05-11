def common(arr1, arr2):
    for x in arr1:
      for y in arr2:
        if x == y:
          return True
    return False

a_list = [1, 2, 4, 5, 6]
b_list = [3, 7, 8, 2, 0]

print(common(a_list, b_list))