a_list = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]

def print_mult(arr):
    result = 1
    for x in arr:
        result *= x
    return result

print(print_mult(a_list))