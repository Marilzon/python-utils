import os
os.system('clear')

cars = ["HRV", "GOLF", "ARGO", "CRUZE"]

for car in cars:
    print(10* "-", car)

github = "https://github.com/Marilzon"

count = 0
for letter in github:
    if count < len(github) / 2:
        count = count + 1
    elif count > len(github) / 2:
        count = count + 2
    space = count * " "
    print(space, letter)
print("tobogã link :)")

g = {1:"This", 2:"is", 3:"a", 4:"Dictionary", 5:"loop"} #Dictionary
for key, value in g.items():
    print(30 * '-')
    print('| key: ', key, '|','value:', value)


