def bigsum(*values):
    for value in values:
        result = value + value
    return (result)


def biglist(*values):
    result_list = []
    for value in values:
        result_list.append(value)
    return (result_list)

print(bigsum(1,2,3,4,5))
print(biglist("Marilzon", "Python", "Developer", "and", "data", "specialist"))
