class Cat():
    def __init__(self, name):
        self.name = name


furball = Cat("Grumpy")

print(furball.name)
print("~~~~~~~~~~~~~~~~~~~~~~")


# Inheritance
class Car():
    def exclaim(self):
        print("I am a car!!")


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print("~~~~~~~~~~~~~~~~~~~~~~")


class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor ' + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ', Esquire'


person = Person("Edwin")
doctor = MDPerson('Sonia')
lawyer = JDPerson('Mira')

print(person.name, '\n', doctor.name, '\n', lawyer.name)
print("~~~~~~~~~~~~~~~~~~~~~~")


# get help from parent with super
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name, '\n', bob.email)
print("~~~~~~~~~~~~~~~~~~~~~~")


# Multiple Inheritance
class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())
print("~~~~~~~~~~~~~~~~~~~~~~")


# Mixins
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.name = 'Gilda'
t.feature = 'ichor'
t.age = 'eldritch'
# print a dictionary containing attributes against values
t.dump()

print("~~~~~~~~~~~~~~~~~~~~~~")


# Direct Access
class Duck():
    def __init__(self, input_name):
        self.name = input_name


fowl = Duck("Daffy")
print(fowl.name)
fowl.name = 'Daphne'
print(fowl.name)
print("~~~~~~~~~~~~~~~~~~~~~~")


# Getters and Setters
class Duck2:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("Inside the getter")
        return self.hidden_name

    def set_name(self, input_name):
        print("Inside the setter")
        self.hidden_name = input_name


don = Duck2("Donald")
print(don.get_name())

don.set_name('Donna')
print(don.get_name())
print("~~~~~~~~~~~~~~~~~~~~~~")


# Properties for Attribute Access
# name = property(get_name, set_name)

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("Inside the getter")
        return self.hidden_name

    def set_name(self, input_name):
        print("Inside the setter")
        self.hidden_name = input_name

    name = property(get_name, set_name)


don = Duck('Donald')
print(don.name)
don.name = 'Donna'
print(don.name)
print("~~~~~~~~~~~~~~~~~~~~~~")


# using decorators
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print("Inside the getter")
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print("Inside the setter")
        self.hidden_name = input_name


fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Sonia'
print(fowl.name)
print("~~~~~~~~~~~~~~~~~~~~~~")


# Properties for computed Values
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)
print("~~~~~~~~~~~~~~~~~~~~~~")


# Name Mangling for privacy

class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('Inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck("Howard")
print(fowl.name)
print("~~~~~~~~~~~~~~~~~~~~~~")


# Method types
# 1.0 Class methods
class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, 'little objects.')


easy_a = A()
breezy_a = A()
wheezy_a = A()

A.kids()
print("~~~~~~~~~~~~~~~~~~~~~~")


# 2.0 Static methods
class CoyoteWeapon:
    @staticmethod
    def commercial():
        print("This coyotewepon has been brought to you by Acme")


CoyoteWeapon.commercial()
print("~~~~~~~~~~~~~~~~~~~~~~")
