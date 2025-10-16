# Grandlay-e
# coding: utf-8
# This file contains all the challenges solutions
# Each challenge is implemented as a function

#______________________________2025-08-11_________________________________________
#1 Vowel Balance
"""Given a string, determine whether the number of vowels in the first half of the string is equal 
to the number of vowels in the second half."""
def is_balanced(s):
    vowels = 'aoiueAOIUE'
    mid = len(s) // 2
    midSecondIndex = mid if len(s) % 2 == 0 else mid + 1
    return sum(1 for char in s[:mid] if char in vowels) == sum(1 for char in s[midSecondIndex:] if char in vowels)

#______________________________2025-08-12_________________________________________
#Base check
    """Given a string representing a number, and an integer base from 2 to 36, 
    determine whether the number is valid in that base.
    """
def is_valid_number(n, base):
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
    n = n.upper()
    return all(char in valid_chars for char in n)