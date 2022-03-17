# to error in division
# toggle or comment except to print error message

numbers = [1, 10]

try:
    10 / 1 # pass
    number = numbers[1] # pass
    #  = a # commented to pass
except ZeroDivisionError as err:
    print("Error:", err)
except IndexError as err:
    print("Error:", err)
except BaseException as err:
    print("Error:", err)
else:
    print('Try, except passed')
