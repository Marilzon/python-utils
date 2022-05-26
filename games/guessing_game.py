import random
import os

error_count = 0
winner_number = random.randrange(0, 100)

player_number = int(input("Input a NUMBER: "))
while player_number != winner_number:
    error_count += 1
    os.system("clear")
    if (winner_number > player_number):
        print("Wrong!, this value is bigger, errors: ", error_count)
    elif (winner_number < player_number):
        print("Wrong!, this value is smaller, ", error_count)
    player_number = int(input("Input next NUMBER: errors: "))
print("you win, the right number is: ",  str(player_number))
print("you used", str(error_count + 1), "attempts")
