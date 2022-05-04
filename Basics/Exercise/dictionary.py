# 8.1
print('~~~~~~~~~~~~~~~')
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

# 8.2
print(e2f['walrus'])
print('~~~~~~~~~~~~~~~')

# 8.3
f2e = {french: english for english, french in e2f.items()}
print((f2e))
print('~~~~~~~~~~~~~~~')

# 8.4
print(f2e['chien'])
print('~~~~~~~~~~~~~~~')

# 8.5
print(set(e2f))
print('~~~~~~~~~~~~~~~')

# 8.6
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'enums': {}
    },
    'plants': {},
    'other': {},
}

# 8.7
print(list(life.keys()))
print('~~~~~~~~~~~~~~~')

# 8.8 
print(list(life['animals'].keys()))
print('~~~~~~~~~~~~~~~')

# 8.9
print(list(life['animals']['cats']))
print('~~~~~~~~~~~~~~~')

# 8.10
squares = {number : number**2 for number in range(10)}
print((squares))
print('~~~~~~~~~~~~~~~')


# 8.11
odd = {number for number in range(10) if number % 2 == 1}
print(odd)
print('~~~~~~~~~~~~~~~')

# 8.12

# 8.13
tuple1 = ('optimist', 'pessimist', 'troll')
tuple2 = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
stuff = {key: value for key, value in zip(tuple1, tuple2)}
print(stuff)