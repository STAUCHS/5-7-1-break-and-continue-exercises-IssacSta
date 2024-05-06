#-------------------------------------------------------------------------
# Name: Issac zha
# Purpose:entering bank pin
# Author:     Zha. I
# Created:    06/05/2024
#-------------------------------------------------------------------------

def main():
    correct_pin = "1938"

    print("WELCOME TO STA BANK!")

    while True:
        user_pin = input("\nEnter your PIN: ")

        if user_pin == correct_pin:
            print("PIN accepted. You may now access your account.")
            break  
        else:
            print("Incorrect PIN. Try again.")
