#Dice Rolling Code

import random

dice = {"d3": 3, 
        "d4": 4,
        "d5": 5,
        "d6": 6,
        "d8": 8,
        "d10": 10,
        "d12": 12,
        "d20": 20,
        "d100": 100
        }

def get_dice_choice():
    while True: 
        dice_choice = input("What dice would you like to roll? (ex: d6) ")
        if dice_choice in dice:
            print(f'you chose to roll the {dice[dice_choice]}')
            return dice_choice
        else:
            print("invalid format")

def get_dice_quantity():
    while True:
        try:
            dice_quantity = int(input("How many would you like to roll? (integer value) "))
            if dice_quantity <= 0:
                print("Please enter a positive integer.")
                continue
            return dice_quantity
        except ValueError:
            print("Please enter a valid integer.")

def roll_dice(dice_quantity, dice_choice):
    total = 0
    for i in range(dice_quantity):
        roll = random.randint(1, dice[dice_choice])
        print(f'{roll}')
        total += roll
    return total
    
def display_roll_sum(total):
    print(f'Sum of dice: {total}')

def run_dice_roller():
    while True:

        dice_choice = get_dice_choice()

        dice_quantity = get_dice_quantity()

        total = roll_dice(dice_quantity, dice_choice)

        display_roll_sum(total)

        break

run_dice_roller()




