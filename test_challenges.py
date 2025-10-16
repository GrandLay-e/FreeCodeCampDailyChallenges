from challenges import *

#____________________________________________________________
# Test cases for is_balanced function 
def test_is_balanced_racecar():
    assert is_balanced("racecar") is True

def test_is_balanced_lorem_ipsum():
    assert is_balanced("Lorem Ipsum") is True

def test_is_balanced_kitty_ipsum():
    assert is_balanced("Kitty Ipsum") is False

def test_is_balanced_string():
    assert is_balanced("string") is False

def test_is_balanced_space():
    assert is_balanced(" ") is True

def test_is_balanced_alphabet():
    assert is_balanced("abcdefghijklmnopqrstuvwxyz") is False

def test_is_balanced_special_chars():
    assert is_balanced("123A#b!E&*456-o.U") is True