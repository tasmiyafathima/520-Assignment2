# Auto-generated pytest tests for merge_sorted_lists
import importlib
mod = importlib.import_module('outputs.llama3_SelfDebug.merge_sorted_lists')
from outputs.llama3_SelfDebug.merge_sorted_lists import merge_sorted_lists


def test_merge_sorted_lists_1():
    assert merge_sorted_lists([1,3,5],[2,4,6]) == [1,2,3,4,5,6]

def test_merge_sorted_lists_2():
    assert merge_sorted_lists([], [1,2]) == [1,2]

def test_merge_sorted_lists_3():
    assert merge_sorted_lists([], []) == []

def test_merge_sorted_lists_4():
    assert merge_sorted_lists([0,2],[1,3]) == [0,1,2,3]

