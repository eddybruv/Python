def outer(a, b):
    def inner(a, b):
        return a + b
    return 5 + inner(a, b)


print(outer(5, 3))
