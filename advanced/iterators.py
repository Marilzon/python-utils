# two lists
first_name = ['Pietro', 'Zoe', 'Joao', 'Enzo', 'Alice']
actual_age = [1, 3, 2, 1, 5]

for name, age in zip(first_name, actual_age):
    print(f'name: {name}, actual age: {age}')

print('\n')

# in file
with open('ipsum.txt') as ipsum:
    for n, line in enumerate(ipsum, start = 1):
        print(f'{n}  {line.strip()}')

print('\n')

# in dictionaries
user_stack_id = {
    'Pietro': 10,
    'Zoe': 1,
    'Joao': 3,
    'Enzo': 10,
    'Alice': 11
}

for user in user_stack_id.items():
    print(user)

print(f'the bigger stacked id is {max(user_stack_id.values())}')

