op = input("Entry at one basic operation: ")

valueA = int(input("Value: A: "))
valueB = int(input("Value: B: "))
result = 0

if op == "+":
    result = valueA + valueB
elif op == "-":
    result = valueA + valueB
elif op == "/":
    result = valueA + valueB
elif op == "*":
    result = valueA + valueB
else:
    result = "Invalid syntax"

print(valueA, op, valueB, "=", result)

