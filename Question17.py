#17. Number Letter Counts
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def ones_to_strings(number):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    return switcher.get(number)

def tens_to_strings(number):
    switcher = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
    return switcher.get(number)

def hundreds_to_strings(number):
    switcher = {
        0: "zero",
        1: "one hundred",
        2: "two hundred",
        3: "three hundred",
        4: "four hundred",
        5: "five hundred",
        6: "six hundred",
        7: "seven hundred",
        8: "eight hundred",
        9: "nine hundred",
    }
    return switcher.get(number)

def teens_to_strings(number):
    switcher = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
    return switcher.get(number)

def whatIsNumber(number):
    if len(str(number)) == 1:
        return ones_to_strings(number)
    if len(str(number)) == 2:
        if (int(str(number)[-2]) == 1):
            return teens_to_strings(int(str(number)[0:]))
        elif (int(str(number)[-1]) == 0):
            return tens_to_strings(int(str(number)[0]))
        else:
            return tens_to_strings(int(str(number)[-2])), ones_to_strings(int(str(number)[-1]))
    if len(str(number)) == 3:
        if (int(str(number)[-2]) == 0 and int(str(number)[-1]) == 0):
            return hundreds_to_strings(int(str(number)[-3]))
        elif (int(str(number)[-2]) == 1):
            return hundreds_to_strings(int(str(number)[-3])), "and", teens_to_strings(int(str(number)[1:]))
        elif (int(str(number)[-2]) == 0):
            return hundreds_to_strings(int(str(number)[-3])), "and", ones_to_strings(int(str(number)[-1]))
        elif (int(str(number)[-1]) == 0):
            return hundreds_to_strings(int(str(number)[-3])), "and", tens_to_strings(int(str(number)[-2]))
        else:
            return hundreds_to_strings(int(str(number)[-3])), "and", tens_to_strings(int(str(number)[-2])), ones_to_strings(int(str(number)[-1]))
    if len(str(number)) == 4:
        return "one thousand"

def charCount(phrase):
    count = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    phrase = " ".join(phrase)
    for letter in phrase:
        if letter in alpha:
            count += 1
    return count



def totalLetterCount(maxVal):
    count = 0
    for i in range(1, maxVal+1):
        count += charCount(whatIsNumber(i))
    return count


print totalLetterCount(1000)