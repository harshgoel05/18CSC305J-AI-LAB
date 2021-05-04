from itertools import chain, permutations
from string import digits


def solve(arr, result):
    letters = ''.join(set(chain(result, *arr))) #collect all letter (unique) by iterating
    initial_letters = ''.join(set(chain(result[0], (a[0] for a in arr))))
    for perm in permutations(digits, len(letters)): # all permutations loop
        decipher_table = str.maketrans(letters, ''.join(perm))  #perm => numbers perm
        def decipher(s):
            return s.translate(decipher_table) 
        if '0' in decipher(initial_letters):
            continue # as leading zeros not allowed so just skip all
        deciphered_sum = sum(int(decipher(code)) for code in arr) # add both codes
        if deciphered_sum == int(decipher(result)): #check if sum is equal to sum result
            print("---------------------------------------------------------")
            print(str(arr[0]) + "  " + str(decipher(arr[0])))
            print(str(arr[1]) + "  " + str(decipher(arr[1])))
            print(str(result) + "  " + str(decipher(result)))
            print("---------------------------------------------------------")
            break
    else:
        print(" + ".join(arr), "=", result, " : no solution")

# solve(['SEND', 'MORE'], 'MONEY')
solve(['TWO', 'TWO'], 'FOUR')
# solve(['BASE', 'BALL'], 'GAMES')
































# GOAL => Assign each letter unique digit
# Restriction => No digit should repeat
# Restriction => Adding all should be equal to last two

# The goal here is to assign each letter a digit from 0 to 9 so that the arithmetic works out correctly. 
# The rules are that all occurrences of a letter must be assigned the same digit, 
# and no digit can be assigned to more than one letter.

# First, create a list of all the characters that need assigning to pass to Solve
# If all characters are assigned, return true if puzzle is solved, false otherwise
# Otherwise, consider the first unassigned character
# for (every possible choice among the digits not in use)
# make that choice and then recursively try to assign the rest of the characters
# if recursion successful, return true
# if !successful, unmake assignment and try another digit