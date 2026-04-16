"""Palindrome Test with Arraystack"""
from file01 import ArrayStack, Empty

def is_palindrome(input_string):
    
    final_word = ""
    
    stack = ArrayStack()

    if not input_string:
        raise Empty("Cannot perform operation: String is empty")
    
    for char in input_string:
        stack.push(char)
        
    while not stack.is_empty():
        final_word += stack.pop()
        
    return input_string.lower() == final_word.lower()    
    


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print(f"{input_string} is a palindrome")
    else:
        print(f"{input_string} is not a plaindrome")