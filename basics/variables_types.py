a = 1
b = '2'
c = False
d = complex(5, 6) # math complex number expression
e = ["This", "is", "a", "list"]
f = ("This", "is", "a", "tuple")
g = {1:"This", 2:"is", 3:"a", 4:"Dictionary"}
h = {"This", "is", "a", "a", "Set"}

print(30 * "-")
"""
    to print correct attributes,
    'str()' is a implicit cast to convert all values to strings
"""
print("Value "+ str(a) + " type: " + str(type(a)))
print("Value "+ b + " type: " + str(type(b)))
print("Value "+ str(c) + " type: " + str(type(c)))
print("\n")
print("variable d: ",d)
print("Real number ", d.real) # real number
print("Imaginary number ", d.imag) # imaginary number
print("Type of variable d: ", type(d))
print("\n")
print("e: ", e)
print("Type of variable e: ", type(e))
print("\n")
print("f: ", f)
print("Type of variable f: ", type(f))
print("Tuples values are immutables")
print("\n")
print("g: ", g)
print("Type of variable g: ", type(g))
print("\n")
print("h: ", h)
print("Type of variable h: ", type(h))
print("Set type remove all duplicated values and sort by asc")
