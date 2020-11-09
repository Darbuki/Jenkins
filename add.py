import pytest

def add(a,b):
    c = a+b
    return c

def test_add():
    assert add(3,5) == 8
    

wow=3
