from random import *

title_game = '\t\tGUESS THE NUMBER\n'
print(title_game)
print("\tHello! I thought of a number between 1 and 1000")
print("\t\tYOU HAVE 8 LIVES\n\t\tGOOD LUCK ! :)\n")

lives = 8
number = randint(1, 1000)
tries = 0
# print(number)
print(f"LIVES: {lives}")
while lives > 0:
    player = int(input('Enter a number: '))

    tries += 1

    if 1 <= player <= 1000:
        if player > number:
            print("Sorry your number is bigger than my number :(\n")
            lives -= 1
        elif player < number:
            print("Sorry your number is less than my number :(\n")
            lives -= 1
        else:
            print("Your number is correct! :)\n¡¡¡¡ CONGRATULATIONS !!!\n")
            print(f"It took you {tries} turns to guess the number :)")
            print("G A M E   O V E R")
            break
    else:
        print("Number not in range\n")
        lives -= 1

    if lives > 0:
        print(f"LIVES: {lives}")
    else:
        print(f"The number was {number}")
        print("You have no more lives...\nG A M E   O V E R\n\t\t:(")

