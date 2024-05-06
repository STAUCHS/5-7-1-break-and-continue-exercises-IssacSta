#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
def main():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    total = 0
    for num in range(start, end + 1):
        if num == 13 or num == 31:
            break
        total += num

    print("The sum of numbers up to encountering 13 or 31 is:", total)

