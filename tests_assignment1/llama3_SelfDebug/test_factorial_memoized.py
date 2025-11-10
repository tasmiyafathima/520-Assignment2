# Auto-generated pytest tests for factorial_memoized
import importlib
mod = importlib.import_module('outputs.llama3_SelfDebug.factorial_memoized')
from outputs.llama3_SelfDebug.factorial_memoized import factorial_memoized


def test_factorial_memoized_1():
    assert factorial_memoized(5) == 120

def test_factorial_memoized_2():
    assert factorial_memoized(0) == 1

def test_factorial_memoized_3():
    assert factorial_memoized(7) == 5040

def test_factorial_memoized_4():
    assert factorial_memoized(1) == 1

