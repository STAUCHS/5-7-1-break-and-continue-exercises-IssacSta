#-------------------------------------------------------------------------
# Name: Issac zha
# Purpose: roll  2 dices
# Author:     Zha. I
# Created:    06/05/2024
#-------------------------------------------------------------------------

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("HERE COMES THE DICE!\n")

    roll_count = 0

    while True:
        roll_count += 1

        roll1 = roll_dice()
        roll2 = roll_dice()

        print(f"Roll #{roll_count}: {roll1}")
        print(f"Roll #{roll_count}: {roll2}")

        total = roll1 + roll2
        print(f"The total is {total}!\n")

        if roll1 == roll2:
            break