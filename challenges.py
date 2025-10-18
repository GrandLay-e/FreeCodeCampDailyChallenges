# Grandlay-e
# coding: utf-8
# This file contains all the challenges solutions
# Each challenge is implemented as a function

#______________________________2025-08-11_________________________________________
#1 Vowel Balance
def is_balanced(s: str) -> bool:
    """Given a string, determine whether the number of vowels in the first half of the string is equal 
    to the number of vowels in the second half.
    
    Args:
        s (str): input string
        
    Returns:
        bool: True if vowels are balanced, False otherwise
    """
    vowels = 'aoiueAOIUE'
    mid = len(s) // 2
    midSecondIndex = mid if len(s) % 2 == 0 else mid + 1
    return sum(1 for char in s[:mid] if char in vowels) == sum(1 for char in s[midSecondIndex:] if char in vowels)

#______________________________2025-08-12_________________________________________
#Base check
def is_valid_number(n: str, base: int) -> bool:
    """Given a string representing a number, and an integer base from 2 to 36, 
    determine whether the number is valid in that base.
    
    Args:
        n (str): string representation of number
        base (int): base to check against (2-36)
        
    Returns:
        bool: True if the number is valid in the given base, False otherwise
    """
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
    print( valid_chars)
    n = n.upper()
    return all(char in valid_chars for char in n)

#______________________________2025-08-13_________________________________________
#3 Fibonacci Sequence
def fibonacci_sequence(start_sequence: list[int], length: int) -> list[int]:
    """The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
    
    Args:
        start_sequence (list[int]): initial sequence of at least 2 numbers
        length (int): desired length of the sequence
        
    Returns:
        list[int]: fibonacci sequence of specified length
    """
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
def space_jam(s: str) -> str:
    """Given a string, remove all spaces from the string, insert two spaces between every character, 
    convert all alphabetical letters to uppercase, and return the result.
    
    Args:
        s (str): input string
        
    Returns:
        str: formatted string with double spaces between characters
    """
    return '  '.join(s.replace(' ', '').upper())

#______________________________2025-08-15_________________________________________
#5 Jumbled Text
def jbelmu(text: str) -> str:
    """Given a string, return a jumbled version of that string where each word is transformed using the following constraints:
    The first and last letters of the words remain in place
    All letters between the first and last letter are sorted alphabetically.
    The input strings will contain no punctuation, and will be entirely lowercase.
    
    Args:
        text (str): input text to jumble
        
    Returns:
        str: jumbled text
    """
    def jumble_word(word):
        if len(word) <= 2:
            return word
        middle = sorted(word[1:-1])
        return word[0] + ''.join(middle) + word[-1]

    return ' '.join(jumble_word(word) for word in text.split())

# ___________________________________2025-08-16___________________________________________
#6 Anagram Checker
def are_anagrams(str1: str, str2: str) -> bool:
    """Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
    
    Args:
        str1 (str): first string
        str2 (str): second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
    """
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

#____________________________________2025-08-17____________________________________________
#7 Targeted Sum
def find_target(arr: list[int], target: int) -> list[int] | str:
    """Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
    Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
    
    Args:
        arr (list[int]): list of numbers
        target (int): target sum
        
    Returns:
        list[int] | str: indices of the two numbers that add up to target, or error message
    """
    num_to_index = {}
    for index, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return "Target not found"

#___________________________________2025-08-18___________________________________________
#8 Factorializer
def factorial(n: int) -> int:
    """Given an integer from zero to 20, return the factorial of that number. 
    The factorial of a number is the product of all the numbers between 1 and the given number.

    Args:
        n (int): given number

    Returns:
        int: the factorial of that number
    """
    return 1 if n == 0 else n * factorial(n - 1)
