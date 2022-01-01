# Level 6: Find The Parity Outlier
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
#
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
    sum = 0;

    for n in integers:
        sum += abs(n) % 2

    if sum == 1:
        for n in integers:
            if n % 2 == 1:
                return n
    else:
        for n in integers:
            if n % 2 == 0:
                return n

if find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11:
    print(True)
if find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160:
    print(True)
