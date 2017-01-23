"""
Problem:

    Given a list of integers, nums, and two integers, a and b, we would like
    to find out which one occurs most frequently in our list.
    If either a or b appears more often, print that number.
    If neither appears at all, print "Neither".
    If they appear the same number of times, print "Tie".
    

Tests:

    >>> mode([1, 2, 3, 3], 2, 3)
    3
    >>> mode([1, 2, 2, 3, 4], 2, 3)
    2
    >>> mode([1, 2, 2, 1, 2], 3, 4)
    Neither
    >>> mode([2, 2, 3, 3], 2, 3)
    Tie
    >>> mode([], 1, 2)
    Neither

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 


def mode(nums, a, b):

    if nums.count(a) > nums.count(b):
        print(a)

    elif nums.count(b) > nums.count(a):
        print(b)

    elif nums.count(a) == nums.count(b) and  nums.count(a) > 1 and nums.count(b) >1:
        print("Tie")

    else:
        print("Neither")


