# A set is like a dictionary of values, excluding keys
# sets are unordered
# it doesn't contain any item twice
print(set('letters'))

# get length with len()
print(len(set('letters')))

# delete an item with .remove()
s = set((1, 2, 3))
s.remove(3)
print(s)

print('~~~~~~~~~~~~~~~~~')


# iterate with for and in
furniture = set(('sofa', 'ottaman', 'table'))
for piece in furniture:
    print(piece)

print('~~~~~~~~~~~~~~~~~')

# test for value with in
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, content in drinks.items():
    if 'vodka' in content:
        print(name)

print('~~~~~~~~~~~~~~~~~')

# combinations and operators
# set intersection command, &
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print('~~~~~~~~~~~~~~~~~')

for name, contents in drinks.items(): 
  if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
    print(name)
  
print('~~~~~~~~~~~~~~~~~')

a = {1, 2}
b = {2, 3}

print(f'intersection: ', a & b)
print('~~~~~~~~~~~~~~~')

# get union by using | or the set union() fxn
print('union: ', a | b)
print('~~~~~~~~~~~~~~~')

# get difference by using - or difference() fxn
print('difference: ', a-b)
print('~~~~~~~~~~~~~~~')

# sysmetric difference by using ^ or set symmetric_difference function()
print('symmetric difference: ', a ^ b)
print('~~~~~~~~~~~~~~~')

# check whether one set is the subset of another using <= or issubset()
print('"a" a subset of "b": ', a <= b)
print('~~~~~~~~~~~~~~~')

# check whether one set is a proper subset of another using < 
print('"a" a proper subset of "a": ', a < a)
print('~~~~~~~~~~~~~~~')

# check for superset using >= or .issuperset()
print('"a" a superset of "a": ', a >= a)
print('~~~~~~~~~~~~~~~')

# set comprehensions
# { expression for expression in iterable }
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)
