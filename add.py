import pytest

def add(a,b):
    c = a+b
    return c

def test_add():
    assert add(4,5) == 8
    

wow=3
