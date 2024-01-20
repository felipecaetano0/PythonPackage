import pytest
from src.evaluate import evaluate

def test_01():
    assert evaluate('1+1') == 2


def test_02():
    assert evaluate('[]') == []

def test_03():
    assert evaluate('dict()') == {}
