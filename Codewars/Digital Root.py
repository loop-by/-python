# Level 6: Sum of Digits / Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00
#
# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    while n > 9:
        sum = 0
        for digit in str(n):
            sum += int(digit)
        n = sum
    return n

if digital_root(16) == 7:
    print(True)
if digital_root(942) == 6:
    print(True)
if digital_root(132189) == 6:
    print(True)
if digital_root(493193) == 2:
    print(True)
