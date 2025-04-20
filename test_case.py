from string_calculator import add

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