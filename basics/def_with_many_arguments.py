def bigsum(*values):
    for value in values:
        result = value + value
    print(result)

bigsum(1,2,3,4,5)

def biglist(*values):
    result_list = []
    for value in values:
        result_list.append(value)
    print(result_list)
    print(type(result_list))

biglist("Marilzon", "Python", "Developer", "and", "data", "specialist")
