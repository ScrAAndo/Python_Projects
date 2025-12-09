#Dice Rolling Code

import random
import re

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

while True:  
        dice_choice = input("What dice would you like to roll? (ex: d6) ")
        if dice_choice in dice:
            dice_quantity = int(input("How many would you like to roll? (integer value) "))
            sum = 0
            for i in range(dice_quantity):
                roll = random.randint(1, dice[dice_choice])
                print(f'{roll}')
                sum += roll
            print(f'Sum of dice: {sum}')
            break
        else:
            print("invalid format")




