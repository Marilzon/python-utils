import time
import os

os.system("clear")

count = 0
github = "https://github.com/Marilzon"

print(len(github) * "-")

while count < len(github):
    print(count * " ",github[count])
    count = count + 1
    time.sleep(0.05)

print(len(github) * "-")
