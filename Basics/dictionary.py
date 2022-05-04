# create dictionaries using curly braces
import copy
bierce = {
    "day": 'A period of twenty-four hours, mostly misspent',
    "positive": "Mistaken at the tpo of one's voice",
    "misfortune": "The kind of fortune that never misses",
}

# create dictionary using dict()
acme_customer = dict(first="Wile", middle="E", last="Coyote")

# use dict fxn to convert two value sequences into a dictionary
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
dict(lol)

# a list of two-item tuples:
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
dict(lot)

# add or change item by [key]
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print(f'Pythons: \n{pythons} \n')
pythons['Gilliam'] = 'Terry'
print(f'After modification Pythons: {pythons}')

# use 'in to check for a key in a dictionary
print('Eric' in pythons)

# use .get() to get key value, if it exists
print(pythons.get('Chapman', 'Not in pythons'))

# use list() to avoid dict_stuff
# get all keys with .keys()
print(pythons.keys())

# get all values with .values()
print(pythons.values())

# get all key-value pairs with .items()
print((pythons.items()))

# get length with len()
print(len(pythons))

# combine dictionaries with {**a, **b}
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})

# combine dictionaries with update()
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

# delete an item by key with del
del pythons['Chapman']
print(pythons)

# get item by key and delete with pop
print(len(pythons))
pythons.pop('Palin')
print(len(pythons))
# giving pop a second argument, the dictionary is not changed

# delete all items with clear()
pythons.clear()

# if you make a change to a dictionary, it will be reflected in all the names that refer to it

# copy with copy()
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}

other_signals = signals.copy()
print(other_signals)

# copy everything with deepcopy()
signals = {
    'green': 'go',
    'yellow': 'go faster', 
    'red': ['stop', 'smile']
}

signals_copy = copy.deepcopy(signals);

# Dictionary comprehensions
# {key_expression : value_expression for expression in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

# {key_expression : value_expression for expression in iterable if condition}
vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)