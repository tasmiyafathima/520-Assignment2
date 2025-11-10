# Auto-generated pytest tests for count_anagrams
import importlib
mod = importlib.import_module('outputs.llama3_SelfDebug.count_anagrams')
from outputs.llama3_CoT.count_anagrams import count_anagrams


def test_count_anagrams_1():
    assert count_anagrams(['eat','tea','tan','ate','nat','bat']) == {('a','e','t'):3, ('a','n','t'):2, ('a','b','t'):1}

def test_count_anagrams_2():
    assert count_anagrams(['listen','silent','enlist']) == {('e','i','l','n','s','t'):3}

def test_count_anagrams_3():
    assert count_anagrams(['rat','tar','art']) == {('a','r','t'):3}

def test_count_anagrams_4():
    assert count_anagrams(['a','b','c']) == {('a',):1, ('b',):1, ('c',):1}

