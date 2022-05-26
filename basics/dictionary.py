import os
from time import sleep

os.system('clear')

g = {1: 'This', 2: 'is', 3: 'a', 4: 'Dictionary'}  # Dictionary

g_plus = {
    1:
    {
        '1.1': 'Im Submenu',
        '1.2': 'Im Submenu 2'
    },
    '2':
    {
        '2.1': 'Hi, I am second Submenu',
        '2.2': 'Im, I am secondSubmenu 2',
        '2.3':
        {
            '2.3.1': 'Easter Egg'
        }
    }
}  # Dictionary with submenus

print('\n')
sleep(0.5)
# Getting values

print(g)

print(g_plus)

print(g[1])  # By indexes
print(g[2])
print(g[3])
print(g[4])


print('\n')
sleep(0.5)

print(g.get(1))  # By get function
print(g.get(2))
print(g.get(3))
print(g.get(4))

print('\n')
sleep(0.5)

sleep(0.5)
for key, value in g.items():
    print(30 * '-')
    print('| key: ', key, '|', 'value:', value)

print('\n')
sleep(0.5)

g.pop(1)
print('g.pop(1) - Removing first position')
print(g)

print('\n')
sleep(0.5)

g.clear()
print('g.clear() - Removing last position')
print(g)
