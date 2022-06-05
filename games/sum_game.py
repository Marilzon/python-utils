import random
import os

os.system("clear")

def sum_game():
    error_count = 0
    x = random.randrange(0, 100)
    y = random.randrange(0, 100)
    print("Answer the sum: ", x, "+", y, " = ", "?")
    result = x + y
    player_result = int(input("Input the result: "))

    while player_result != result:
        error_count += 1
        if (result > player_result):
            print("Wrong!, this value is bigger, errors: ", error_count)
        elif (result < player_result):
            print("Wrong!, this value is smaller, ", error_count)
        player_result = int(input("Try new response: "))
    print("---you win---, the result is: ",  str(player_result))
    print("you used", str(error_count + 1), "attempts")

    return

sum_game()
