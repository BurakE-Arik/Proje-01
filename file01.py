# İlk bağımsız OOP denemem 13/04/2026
class Empty(Exception):
    pass

class ArrayStack:
    """ Implement a stack object with python list"""
    
    def __init__(self):
        """Implement stack"""
        
        self._data = []
               
    def __len__(self):
        """Return lenght of stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return true if stack is empty"""
        return not self._data
    
    def push(self,e):
        """Add an element into stack"""
        self._data.append(e)
        
    def pop(self):
        """Remove item LIFO principle"""
        if self.is_empty():
            raise Empty("Cannot perform operation: Stack is empty")
        
        return self._data.pop()
    
    def __str__(self):
        """Return string of stack"""
        return f"{self._data} < Top"
    
    