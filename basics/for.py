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


