# Auto-generated pytest tests for matrix_rotate_90
import importlib
mod = importlib.import_module('outputs.llama3_SelfDebug.matrix_rotate_90')
from outputs.llama3_SelfDebug.matrix_rotate_90 import matrix_rotate_90


def test_matrix_rotate_90_1():
    assert matrix_rotate_90([[1,2],[3,4]]) == [[3,1],[4,2]]

def test_matrix_rotate_90_2():
    assert matrix_rotate_90([[1]]) == [[1]]

def test_matrix_rotate_90_3():
    assert matrix_rotate_90([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]

def test_matrix_rotate_90_4():
    assert matrix_rotate_90([[1,2],[3,4]]) == [[3,1],[4,2]]

