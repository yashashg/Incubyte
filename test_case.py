from string_calculator import add
import pytest

def test_empty_string():
    assert add("") == 0 

# Adding a new failed test case
def test_simple_number():
    assert add("7") == 7

#Adding two numbers, Seperated by comma

def test_multiple_number():
    assert add("7,3") == 10

def test_many_number():
    assert add("7,3,10,6") == 26

def test_newlines_number():
    assert add("7,3\n4,6") == 20

def test_newlines_number():
    assert add("//;\n1;2") == 3

def test_negative_number_raises_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed -12"):
        add("10,-12")

def test__multiple_negative_number():
    with pytest.raises(ValueError, match="negative numbers not allowed -12,-5,-10"):
        add("10,-12,-5,9,-10")

