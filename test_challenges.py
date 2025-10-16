# This file contains test cases for the functions defined in challenges.py
# The tests are written using the pytest framework
# And they're all getted from the examples provided in the challenges description
from challenges import *

#1________________________2025-08-11____________________________________
# Test cases for is_balanced function 
def test_is_balanced_racecar():assert is_balanced("racecar") is True
def test_is_balanced_lorem_ipsum():assert is_balanced("Lorem Ipsum") is True
def test_is_balanced_kitty_ipsum():assert is_balanced("Kitty Ipsum") is False
def test_is_balanced_string():assert is_balanced("string") is False
def test_is_balanced_space():assert is_balanced(" ") is True
def test_is_balanced_alphabet():assert is_balanced("abcdefghijklmnopqrstuvwxyz") is False
def test_is_balanced_special_chars():assert is_balanced("123A#b!E&*456-o.U") is True

#2________________________2025-08-12____________________________________
# Test cases for is_valid_number function
def test_is_valid_number_binary_true(): assert is_valid_number("10101", 2) is True
def test_is_valid_number_binary_false(): assert is_valid_number("10201", 2) is False
def test_is_valid_number_octal_true(): assert is_valid_number("76543210", 8) is True
def test_is_valid_number_octal_false(): assert is_valid_number("9876543210", 8) is False
def test_is_valid_number_decimal_true(): assert is_valid_number("9876543210", 10) is True
def test_is_valid_number_decimal_false(): assert is_valid_number("ABC", 10) is False
def test_is_valid_number_hex_true(): assert is_valid_number("ABC", 16) is True
def test_is_valid_number_base36_true(): assert is_valid_number("Z", 36) is True
def test_is_valid_number_base20_true(): assert is_valid_number("ABC", 20) is True
def test_is_valid_number_hex2_true(): assert is_valid_number("4B4BA9", 16) is True
def test_is_valid_number_hex2_false(): assert is_valid_number("5G3F8F", 16) is False
def test_is_valid_number_base17_true(): assert is_valid_number("5G3F8F", 17) is True
def test_is_valid_number_lowercase_false(): assert is_valid_number("abc", 10) is False
def test_is_valid_number_lowercase_hex_true(): assert is_valid_number("abc", 16) is True
def test_is_valid_number_mixedcase_hex_true(): assert is_valid_number("AbC", 16) is True
def test_is_valid_number_lowercase_base36_true(): assert is_valid_number("z", 36) is True