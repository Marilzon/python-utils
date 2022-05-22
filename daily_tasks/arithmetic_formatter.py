# FreeCodeCamp Python task
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
import re

def arithmetic_arranger(problems, solve = False):
    if (len(problems) > 5):
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    calcx = ""
    string = ""

    for item in problems:
        if (re.search("[^\s0-9.+-]", item)):
            if(re.search("[/]", item) or re.search("[*]", item)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        first_number = item.split(" ")[0]
        operator = item.split(" ")[1]
        second_number = item.split(" ")[2]

        if (len(first_number) >= 5 or len(second_number) >= 5):
            return "Error: Numbers cannot be more than four digits."

        calc = ""
        if (operator == "+"):
            calc = str(int(first_number) + int(second_number))
        elif (operator == "-"):
            calc = str(int(first_number) - int(second_number))

        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""
        response = str(sum).rjust(length)
        for s in range(length):
            line += "-"

        if item != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            calcx += response
        else:
            first += top
            second += bottom
            lines += line
            calcx += response

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + calcx
    else:
        string = first + "\n" + second + "\n" + lines
    return string
