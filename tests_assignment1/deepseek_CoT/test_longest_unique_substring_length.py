# Auto-generated pytest tests for longest_unique_substring_length
import importlib
mod = importlib.import_module('outputs.deepseek_CoT.longest_unique_substring_length')
from outputs.deepseek_CoT.longest_unique_substring_length import longest_unique_substring_length


def test_longest_unique_substring_length_1():
    assert longest_unique_substring_length('abcabcbb') == 3

def test_longest_unique_substring_length_2():
    assert longest_unique_substring_length('bbbbb') == 1

def test_longest_unique_substring_length_3():
    assert longest_unique_substring_length('pwwkew') == 3

def test_longest_unique_substring_length_4():
    assert longest_unique_substring_length('dvdf') == 3

