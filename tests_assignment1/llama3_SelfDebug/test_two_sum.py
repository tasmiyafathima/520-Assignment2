# Auto-generated pytest tests for two_sum
import importlib
mod = importlib.import_module('outputs.llama3_SelfDebug.two_sum')
from outputs.llama3_SelfDebug.two_sum import two_sum


def test_two_sum_1():
    assert set(two_sum([2,7,11,15], 9)) == {0,1}

def test_two_sum_2():
    assert set(two_sum([3,2,4], 6)) == {1,2}

def test_two_sum_3():
    assert set(two_sum([3,3], 6)) == {0,1}

def test_two_sum_4():
    assert set(two_sum([1,5,3,2], 7)) == {1,3}

