import os
os.system("clear")

# basic sintax
def loop(recursion):
    if recursion > 0:
        print(f'recursion activated {recursion}')
        loop(recursion - 1)
loop(15)

print('\n')

# traditional fibonacci using for statement
previous = 0
print(previous)
last = 1
print(last)

for i in range(1, 10):
    next = last + previous
    previous = last
    last = next
    print(next)

print('\n')

# fibonacci using recursion
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (fibonacci(n - 1) + fibonacci(n - 2))

print(fibonacci(3))
