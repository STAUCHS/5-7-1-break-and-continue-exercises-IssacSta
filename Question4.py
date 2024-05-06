#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
def main():
    while True:
        word = input("Enter a word: ")
        print(f"Your word: {word}")

        if word.lower() == "stop":
            break

    print("Goodbye!")
