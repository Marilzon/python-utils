def evens():
    x = 0
    while x < 20:
        x += 2
        yield x

def odds():
    x = -1
    while x < 20:
        x += 2
        yield x

def chain(x, y):
    yield from x
    yield from y

for value in chain(evens(), odds()):
    print(value)
