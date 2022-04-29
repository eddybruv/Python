# tuples using commas
names = 'Sonia', 'Edwin', 'Nesa',
print(names)

# tuples using brackets ()
names = ('Edwin', 'Gilda', 'Obi',)
print(names)

# destructuring a tuple
name1, name2, name3 = names
print(f'{name1}, {name2}')

# create tuple with tuple()
word = "How are we doing"
print(tuple(word))

# looping a tuple
numbers = (1, 2, 3, 4, 5, 6)
for number in numbers:
    if number % 2 == 0:
        print(number * 2)

# modifying tuples

