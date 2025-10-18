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
    print( valid_chars)
    n = n.upper()
    return all(char in valid_chars for char in n)

#______________________________2025-08-13_________________________________________
#3 Fibonacci Sequence
    """The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
    """
def fibonacci_sequence(start_sequence, length):
    if length <= 0:
        return []
    elif length <= len(start_sequence):
        return start_sequence[:length]
    
    sequence = start_sequence[:]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

#______________________________2025-08-14_________________________________________
#4 S P A C E J A M
    """Given a string, remove all spaces from the string, insert two spaces between every character, 
    convert all alphabetical letters to uppercase, and return the result.
    """
def space_jam(s):
    return '  '.join(s.replace(' ', '').upper())

#______________________________2025-08-15_________________________________________
#5 Jumbled Text
    """Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

    The first and last letters of the words remain in place
    All letters between the first and last letter are sorted alphabetically.
    The input strings will contain no punctuation, and will be entirely lowercase.
    """
def jbelmu(text):
    def jumble_word(word):
        if len(word) <= 2:
            return word
        middle = sorted(word[1:-1])
        return word[0] + ''.join(middle) + word[-1]

    return ' '.join(jumble_word(word) for word in text.split())

# ___________________________________2025-08-16___________________________________________
#6 Anagram Checker
    """Given two strings, determine if they are anagrams of each other (contain the same characters in any order)."""
def are_anagrams(str1, str2):
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

#____________________________________2025-08-17____________________________________________
#7 Targeted Sum
    """Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
    Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
    """
def find_target(arr, target):
    num_to_index = {}
    for index, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return "Target not found"