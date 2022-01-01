# Create a function taking a positive integer as its parameter and
# returning a string containing the Roman Numeral representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and
# skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC;
# resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: M DC LX VI.

def solution(n):
    output = ""
    counter = 0

    while n >= 1000:
        counter += 1
        n -= 1000

    while n >= 500:
        output += "D"
        n -= 500

    while n >= 100:
        output += "C"
        n -= 100

    while n >= 50:
        output += "L"
        n -= 50

    while n >= 10:
        output += "X"
        n -= 10

    while n >= 5:
        output += "V"
        n -= 5

    while n >= 1:
        output += "I"
        n -= 1

    return output

print(solution(1666))
