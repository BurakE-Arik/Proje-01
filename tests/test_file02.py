from file02 import reverse_stack

def test_reverse_stack_func():
    
    assert str(reverse_stack("Burak")) == "['k', 'a', 'r', 'u', 'B'] < Top"
    assert str(reverse_stack("racecar")) == "['r', 'a', 'c', 'e', 'c', 'a', 'r'] < Top"
    
