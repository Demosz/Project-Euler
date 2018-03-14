# 11. Finding teh largest product of four adjacent numbers in the same direction.
"""
What is the greatest product of four adjacent numbers in the same direction in the 20x20 grid?
"""

"""
I will have to create a grid of the listed numbers. To do that, I will copy the numbers into a text file, and open the 
text file to read its contents into a Python dictionary. From there, I will space out that dictionary so each number has
an X and a Y coordinate. Once my grid is complete, I will create a function that checks for numbers in each cardinal
direction, multiplies them, and checks the result with a global maximum value. If that result exceeds the current max,
it will become the maximum value. The final maximum value will be returned at the end.
"""

#These initial declarations will establish my grid. The 'with' statement will open the text file and append numbers to
# a list. The 'for' loop will then send each of those numbers to a key (size 20) in a dictionary, creating a nice, neat
# for me to iterate through with an (X,Y) selector.
test = {}
numlist = []
linecount = 0
global high
high = 0


with open("numbers.txt", "r") as f:
    for line in f:
        for i in range(0, len(line), 3):
            numlist.append(int(line[i:i + 2]))

for i in range(20):
    test[i] = []
    for e in range(20):
        test[i].append(numlist[linecount + e])
    linecount += 20


"""
This function takes an X and Y input and returns the value at that point in the grid. The Y value starts from the top!
"""
def num(x, y):
    xin = (x)
    yin = (y)
    value = test[yin][xin]
    return value

"""
All following functions test a number to see if it has 3 following numbers in a certain direction. If it has them, 
it harvests those numbers and multiplies them, testing the result against the global maximum value.
"""

def getFourUp(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (y - i) >= 0:
            sum.append(num(x, (y - i)))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high

def getFourDown(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (y + i) >= 0:
            sum.append(num(x, (y + i)))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high

def getFourLeft(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (x - i) >= 0:
            sum.append(num((x - i), y))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high

def getFourRight(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (x + i) < 20:
            sum.append(num((x + i), y))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high

def getFourUpRight(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (x + i) < 20 and (y - i) >= 0:
            sum.append(num((x + i), (y - i)))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high

def getFourDownRight(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (x + i) < 20 and (y + i) < 20:
            sum.append(num((x + i), (y + i)))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high

def getFourUpLeft(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (x - i) >= 0 and (y - i) >= 0 :
            sum.append(num((x - i), (y + i)))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high


def getFourDownLeft(x, y):
    global high
    sum = []
    total = 1
    for i in range(0, 4):
        if (x - i) > 0 and (y + i) < 20 :
            print num((x - i), (y + i))
            sum.append(num((x - i), (y + i)))
    print sum
    for val in sum:
        total = total * val
    print total
    if total > high:
        high = total
        print high


"""
This function cycles through every previous function and attempts to call it for the given value of X, Y. 
"""

def attempt(x, y):
    try:
        getFourUp(x, y)
    except:
        return
    try:
        getFourDown(x, y)
    except:
        return
    try:
        getFourLeft(x, y)
    except:
        return
    try:
        getFourRight(x, y)
    except:
        return
    try:
        getFourUpLeft(x, y)
    except:
        return
    try:
        getFourUpRight(x, y)
    except:
        return
    try:
        getFourDownLeft(x, y)
    except:
        return
    try:
        getFourDownRight(x, y)
    except:
        return

"""
This last function cycles through every possible position in the grid, tries to call the previous function, cycling 
through all directions. It returns the maximum value for each position, in each direction, on the grid.
"""

def rundown():
    for y in range(20):
        for x in range(20):
            attempt(x, y)
    global high
    print high, "!!!"

rundown()
