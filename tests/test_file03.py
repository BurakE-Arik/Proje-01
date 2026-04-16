import pytest
from file03 import is_palindrome,Empty

def test_positive_is_palindrome():
    
    assert is_palindrome("Ütü") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("ütü") == True
    
def test_negative_is_palindrome():
    
    assert is_palindrome("Burak") == False
    assert is_palindrome("burak") == False
    assert is_palindrome("araba") == False
    
def edge_case_is_palindrome():
    
    assert is_palindrome("üTü") == True
    
    with pytest.raises(Empty):
        is_palindrome("")
        
    with pytest.raises(Empty) as excinfo:
        is_palindrome("")
        
    assert "Cannot perform operation: String is empty" in str(excinfo.value)