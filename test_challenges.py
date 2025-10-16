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

#3________________________2025-08-13____________________________________
# Test cases for fibonacci_sequence function
def test_fibonacci_sequence_20():
    assert fibonacci_sequence([0, 1], 20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
def test_fibonacci_sequence_single():
    assert fibonacci_sequence([21, 32], 1) == [21]
def test_fibonacci_sequence_zero():
    assert fibonacci_sequence([0, 1], 0) == []
def test_fibonacci_sequence_two():
    assert fibonacci_sequence([10, 20], 2) == [10, 20]
def test_fibonacci_sequence_large_numbers():
    assert fibonacci_sequence([123456789, 987654321], 5) == [123456789, 987654321, 1111111110, 2098765431, 3209876541]

#4________________________2025-08-14____________________________________
# Test cases for space_jam function
def test_space_jam_freecodecamp():assert space_jam("freeCodeCamp") == "F  R  E  E  C  O  D  E  C  A  M  P"
def test_space_jam_spaces():assert space_jam("   free   Code   Camp   ") == "F  R  E  E  C  O  D  E  C  A  M  P"
def test_space_jam_hello_world():assert space_jam("Hello World?!") == "H  E  L  L  O  W  O  R  L  D  ?  !"
def test_space_jam_special_chars():assert space_jam("C@t$ & D0g$") == "C  @  T  $  &  D  0  G  $"
def test_space_jam_allyourbase():assert space_jam("allyourbase") == "A  L  L  Y  O  U  R  B  A  S  E"