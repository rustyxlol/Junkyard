"""
Write a Python program that outputs all possible strings formed by 
using the characters c , a , t , d , o , and g exactly once
"""
from itertools import permutations
from math import factorial


# Approach one: Cheating


def possibilities(lst):
    for item in permutations(lst):
        print("".join(item), end=',')

# Approach two: circular strings


def possibilities2(lst):
    total_permutations = factorial(len(lst))
    all_permutations = []

    for i in range((total_permutations//2)):
        all_permutations.append("".join(lst[i:] + lst[:i]))

    for i in range((total_permutations//2)):
        all_permutations.append("".join(lst[i::-1] + lst[:i:-1]))

    print(all_permutations)


#! Approach three: Recursion - Pending


if __name__ == "__main__":
    possibilities(['c', 'a', 't', 'd', 'o'])
    possibilities2(['c', 'a', 't', 'd', 'o'])
