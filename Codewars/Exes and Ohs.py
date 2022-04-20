# Level 7: Exes and Ohs
# https://www.codewars.com/kata/55908aad6620c066bc00002a/solutions/python
#
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    num_o = 0
    for c in s.lower():
        if c == "o":
            num_o += 1
        elif c == "x":
            num_o -= 1
    return True if num_o == 0 else False

print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))
