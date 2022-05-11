def function(arr):
    count = 0
    for x in arr:
        if len(x) > 2 and x[0] == x[len(x) - 1]:
            count += 1
    return count


a_list = ['abc', 'xyz', 'aba', '1221']
print(function(a_list))
