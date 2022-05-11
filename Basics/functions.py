def do_nothing():
    pass


do_nothing()


def make_sound():
    print('Quack')


make_sound()
print('~~~~~~~~~~~~~~~')


def agree():
    return True


if agree():
    print("Splendid")
else:
    print("That was unexpected")

print('~~~~~~~~~~~~~~~')


def echo(anything):
    return anything + "" + anything


print(echo('Rumplestilskin'))
print('~~~~~~~~~~~~~~~')


def commentary(color):
    if color == 'red':
        return 'Its a tomato'
    elif color == 'green':
        return 'Its a green pepper'
    elif color == 'bee purple':
        return 'I dont know what it is, but only bees can see it'
    else:
        return 'Ive never heard of the color' + color + '.'


comment = commentary('blue')
print(comment)
print('~~~~~~~~~~~~~')

# none is useful
thing = None
if thing is None:
    print("It's some thing")
else:
    print("It's nothing")
print('~~~~~~~~~~~~~')


def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


whatis(None)
whatis(True)
whatis(False)
print('~~~~~~~~~~~~~')
whatis(0)
whatis(0.0)
whatis('')
whatis(())
whatis([])
whatis({})
whatis(set())
whatis(0.00002)
whatis([0])
whatis([''])
print('~~~~~~~~~~~~~')

# Positional Arguments


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))
print('~~~~~~~~~~~~~')

# Keyword Arguments
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print('~~~~~~~~~~~~~')

# Specify Default Paramenter Values


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken'))
print('~~~~~~~~~~~~~')

# mutable default paramenters (list)


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a')
buggy('b')  # expect ['b']
print('~~~~~~~~~~~~~')

# Explode/Gather Positional Arguments with *


def print_args(*args):
    print("positional tuple:", args)


print_args(3, 2, 1, 'uh', 'wait!')
print('~~~~~~~~~~~~~')


def print_more(required1, required2, *args):
    print("need this one:", required1)
    print("need this one too:", required2)
    print("All the rest:", args)


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
print('~~~~~~~~~~~~~')


# Explode/Gather Keyword Arguments with **
def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)


print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
print('~~~~~~~~~~~~~')

# Keyword-Only Arguments


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print('~~~~~~~~~~~~~')

# Mutable and immutable Arguments
outside = ['one', 'fine', 'day']


def mangle(arg):
    arg[1] = 'terrible!'
    print(arg)


mangle(outside)
print('~~~~~~~~~~~~~')
