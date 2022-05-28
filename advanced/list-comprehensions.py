import os
os.system('clear')

first_list = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        first_list.append((x, y))  # Tuple transformation
print(f'{first_list = } ')

print('\n')

second_list = [
    (x, y) for x in range(0, 100, 10)
    for y in range(100, 200, 10)
]
print(f'{second_list = }')

print('\n')

third_list = [[x for x in range(10)] for y in range(3)]
print(f'{third_list = }')
