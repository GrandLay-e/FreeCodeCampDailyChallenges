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

#5________________________2025-08-15____________________________________
# Test cases for jumble_text function
def test_jumble_text_hello_world(): assert jbelmu("hello world") == "hello wlord"
def test_jumble_text_love_jumbled_text(): assert jbelmu("i love jumbled text") == "i love jbelmud text"
def test_jumble_text_freecodecamp(): assert jbelmu("freecodecamp is my favorite place to learn to code") == "faccdeeemorp is my faiortve pacle to laern to cdoe"
def test_jumble_text_quick_brown_fox(): assert jbelmu("the quick brown fox jumps over the lazy dog") == "the qciuk borwn fox jmpus oevr the lazy dog"

#6________________________2025-08-16____________________________________
# Test cases for areAnagrams function
def test_are_anagrams_listen_silent(): assert are_anagrams("listen", "silent") is True
def test_are_anagrams_school_master(): assert are_anagrams("School master", "The classroom") is True
def test_are_anagrams_gentleman(): assert are_anagrams("A gentleman", "Elegant man") is True
def test_are_anagrams_hello_world(): assert are_anagrams("Hello", "World") is False
def test_are_anagrams_apple_banana(): assert are_anagrams("apple", "banana") is False
def test_are_anagrams_cat_dog(): assert are_anagrams("cat", "dog") is False

#7________________________2025-08-17____________________________________
# Test cases for find_target function
def test_find_target_9():assert find_target([2, 7, 11, 15], 9) == [0, 1]
def test_find_target_6():assert find_target([3, 2, 4, 5], 6) == [1, 2]
def test_find_target_15():assert find_target([1, 3, 5, 6, 7, 8], 15) == [4, 5]
def test_find_target_not_found():assert find_target([1, 3, 5, 7], 14) == 'Target not found'

#8________________________2025-08-18____________________________________
# Test cases for factorial function
def test_factorial_zero(): assert factorial(0) == 1
def test_factorial_one(): assert factorial(1) == 1
def test_factorial_five(): assert factorial(5) == 120
def test_factorial_ten(): assert factorial(10) == 3628800
def test_factorial_twenty(): assert factorial(20) == 2432902008176640000
def test_factorial_small_numbers(): assert factorial(3) == 6
def test_factorial_small_numbers_2(): assert factorial(4) == 24

#9________________________2025-08-19____________________________________
# Test cases for sum_of_squares function
def test_sum_of_squares_5(): assert sum_of_squares(5) == 55
def test_sum_of_squares_10(): assert sum_of_squares(10) == 385
def test_sum_of_squares_25(): assert sum_of_squares(25) == 5525
def test_sum_of_squares_500(): assert sum_of_squares(500) == 41791750
def test_sum_of_squares_1000(): assert sum_of_squares(1000) == 333833500

#10________________________2025-08-20____________________________________
def test_squares_with_three_1(): assert squares_with_three(1) == 0
def test_squares_with_three_10(): assert squares_with_three(10) == 1
def test_squares_with_three_100(): assert squares_with_three(100) == 19
def test_squares_with_three_1000(): assert squares_with_three(1000) == 326
def test_squares_with_three_10000(): assert squares_with_three(10000) == 4531
