#5. Smallest Multiple
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

test = 2521
found = False

while found == False:
    for i in range(1, 21):
        if test % i != 0:
            break
        else:
            if i == 20:
                found = True
            continue
    test += 1

print test - 1