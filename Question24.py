#24. Lexicographic Sums
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations
of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
def permutation(s):
   if len(s) == 1:
       return [s]
    #This list will be the array in which we find the solution
   perm_list = []
    #This rotates through every possible first value
   for a in s:
    #This isolates remaining values
       remaining_elements = [x for x in s if x != a]
    #This calls the rotation on the remaining elements, whittling them down to their final value which will be returned
    # by 'if len(s) == 1:'
       z = permutation(remaining_elements)
       """After all remaining elements in the permutation are exhuasted, this code will attach those list to their own
        copy of the next value of increasing complexity, forming a new complete list, which is then passed up. 
        This process repeats until we reach the first value. This requires an understanding of how the + operator works
        while appending with lists!"""
       for t in z:
           perm_list.append([a] + t)

   return perm_list

def answer():
    given = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = ''
    solution = permutation(given)
    print solution
    for (i, d) in enumerate(solution):
        if i == 999999:
            for num in d:
                answer += str(num)
    return answer

print answer()