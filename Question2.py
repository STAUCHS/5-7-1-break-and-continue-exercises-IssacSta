#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------
total = 0
for i in range(5, 21):
    if i % 3 == 0:
        continue
    total += i

print(total)
