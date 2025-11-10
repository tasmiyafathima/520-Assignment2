# Auto-generated pytest tests for binary_search
import importlib
mod = importlib.import_module('outputs.llama3_SelfDebug.binary_search')
from outputs.llama3_SelfDebug.binary_search import binary_search


def test_binary_search_1():
    assert binary_search([1,2,3,4,5], 3) == 2

def test_binary_search_2():
    assert binary_search([1,2,3,4,5], 6) == -1

def test_binary_search_3():
    assert binary_search([], 3) == -1

def test_binary_search_4():
    assert binary_search([1,2,3,4,5], 1) == 0

