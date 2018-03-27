#26. Reciprocal Cycles
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
#Brainstorm
def test(number):
    initial = number
    numlist = []
    divided = []
    divisor = 10
    while True:
        numlist.append(divisor/initial)
        divided.append(divisor)
        if divisor % initial == 0:
            break
        if divisor % initial != 0:
            divisor = (divisor % initial) * 10
            if divisor in divided:
                break
    return len(numlist)


solution = (test(i) for i in range(1, 1001))
position = 0
maxVal = 0
for (index, length) in enumerate(solution):
    if length > maxVal:
        maxVal = length
        position = index + 1
print position
print maxVal