"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2
"""


import math

# Approach one, recursion


def divider(number, count=0):
    if number < 2:
        return count
    return divider(number/2, count+1)


# Approach two, log 😎


def divider2(number):
    return int(math.log(number, 2))

# Approach three, amateur


def divider3(number):
    count = 0
    while number > 2:
        number /= 2
        count += 1
    return count


if __name__ == "__main__":
    print(divider(15632))
    print(divider2(15632))
    print(divider3(15632))
