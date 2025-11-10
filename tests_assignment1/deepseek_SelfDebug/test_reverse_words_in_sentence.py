# Auto-generated pytest tests for reverse_words_in_sentence
import importlib
mod = importlib.import_module('outputs.deepseek_SelfDebug.reverse_words_in_sentence')
from outputs.deepseek_SelfDebug.reverse_words_in_sentence import reverse_words_in_sentence


def test_reverse_words_in_sentence_1():
    assert reverse_words_in_sentence('hello world') == 'world hello'

def test_reverse_words_in_sentence_2():
    assert reverse_words_in_sentence('  one   two three ') == 'three two one'

def test_reverse_words_in_sentence_3():
    assert reverse_words_in_sentence('') == ''

def test_reverse_words_in_sentence_4():
    assert reverse_words_in_sentence('single') == 'single'

