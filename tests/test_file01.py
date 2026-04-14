import pytest
from file01 import ArrayStack, Empty


def test_pop_on_empty_stack_raises_error():
    stack = ArrayStack()
    
    with pytest.raises(Empty):
        stack.pop()
        
    with pytest.raises(Empty) as excinfo:
        stack.pop()
        
    assert "Cannot perform operation: Stack is empty" in str(excinfo.value)
    
    
def test_stack_push_and_len():
    
    stack = ArrayStack()
    
    stack.push(10)
    stack.push(20)
    
    assert len(stack) == 2
    assert stack.is_empty() is False
    
def test_stack_pop_order():
    stack = ArrayStack()
    
    stack.push("A")
    stack.push("B")
    
    assert stack.pop() == "B"
    assert stack.pop() == "A"
    assert stack.is_empty() is True
    
    
def test_string_method():
    stack = ArrayStack()
    
    stack.push(10)
    
    assert stack.__str__() == "[10] < Top"
    
    stack.push(20)
    
    assert stack.__str__() == "[10, 20] < Top"
    