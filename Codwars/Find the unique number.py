# Level 6: Find the unique number
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
#
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):

    old_num = arr[0];
    num = arr[1];

    for n in range(2, len(arr)):
        if arr[n] != num:
            if arr[n] == old_num:
                return num
            else:
                return arr[n]
        else:
            if arr[n] == old_num:
                old_num = num; num = arr[n]
            else:
                return old_num

if find_uniq([ 1, 1, 1, 2, 1, 1]) == 2:
    print(True)
if find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55:
    print(True)
