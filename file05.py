"""Stack implementation with doubly linked list"""
from file04 import _DoublyLinkedeBase

class Stack(_DoublyLinkedeBase):    
    
    def push(self, e):
        self._insert_between(e, self._header, self._header._next)

    def __str__(self):
        return self._header._next._element
    
    
stack1 = Stack()
stack1.push(1)
print(stack1.__str__())