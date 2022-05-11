n = int(input('Enter a number: '))

def long_words(arr):
    new_list = []
    for word in arr:
        if len(word) >= n:
            new_list.append(word)
    return new_list


a_list = ['abc', 'xyz', 'aba', '1221']

long = long_words(a_list)

print(long)