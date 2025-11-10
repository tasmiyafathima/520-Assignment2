# Auto-generated pytest tests for is_balanced_parentheses
import importlib
mod = importlib.import_module('outputs.llama3_SelfDebug.is_balanced_parentheses')
from outputs.llama3_SelfDebug.is_balanced_parentheses import is_balanced_parentheses


def test_is_balanced_parentheses_1():
    assert is_balanced_parentheses('()')

def test_is_balanced_parentheses_2():
    assert is_balanced_parentheses('(())()')

def test_is_balanced_parentheses_3():
    assert not is_balanced_parentheses('(()')

def test_is_balanced_parentheses_4():
    assert not is_balanced_parentheses('())(')

