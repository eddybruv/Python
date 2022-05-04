import copy

# getting parts of a list using slice
word = ["please", "listen", 'now']
print(word[0:2])
print('word[::2]: ', word[::2])

# adding an item to the end to the list
word.append('abeg')

# adding an item by offset, first argument is the index
word.insert(0, 'Edwin')

# combine 2 lists with +
word1 = ['Hello', 'there']
word2 = ['Edwin']
print('word1 + word2: ', word1 + word2)

# extending an array using extend
word1.extend(word2)
print(f'Word1 {word1}')

# editing list with offsets
word[0:2] = ['Hello']

# deleting
# using del

# using remove:
word.remove('Hello')
# using pop: returns the value which was specified with the index
word.pop()
# using clear: deletes every element present in the list
word.clear()

word = ['bad', 'boy']
word[0:2] = ['There', 'there']
word[1:2] = ['over']

print('over' in word)

# list.count is used to count the number of times sth occurs in a list
numbers = [1, 1, 1, 2, 3, 4, 5]
print("1 occurs: ", numbers.count(1))
numbers.sort(reverse=True)
print("Numbers in reverse order: ", numbers)
numbers.sort()

# .copy() returns the same list
new_numbers = numbers.copy()
print('new_numbers: ', new_numbers)

# using deepcopy
numbers = [1, 3, 4, 6, [4, 7, 2, 7]]
new_numbers = copy.deepcopy(numbers)
print('Deep copy new numbers: ', new_numbers)

# using zip
numbers = [1, 2, 3, 4]
new_numbers = [6, 7, 8, 9]

for number1, number2 in zip(numbers, new_numbers):
    print('Number1 + number2: ', number1+number2)

# list comprehension
numbers_new = [number * 2 for number in numbers]
print("After comprehension: ", new_numbers)
