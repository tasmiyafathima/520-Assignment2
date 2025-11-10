# Auto-generated pytest tests for word_frequency_counter
import importlib
mod = importlib.import_module('outputs.deepseek_CoT.word_frequency_counter')
from outputs.deepseek_CoT.word_frequency_counter import word_frequency_counter


def test_word_frequency_counter_1():
    assert word_frequency_counter('This is this') == {'this':2, 'is':1}

def test_word_frequency_counter_2():
    assert word_frequency_counter('Hello hello HELLO') == {'hello':3}

def test_word_frequency_counter_3():
    assert word_frequency_counter('One two one') == {'one':2, 'two':1}

def test_word_frequency_counter_4():
    assert word_frequency_counter('') == {}

