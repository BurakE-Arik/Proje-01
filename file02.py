"""Reverse string contain in a stack object"""
from file01 import ArrayStack


def reverse_string(input_string):
    return input_string[::-1].strip()

def reverse_stack(input_string):
    
    reversed_stack = ArrayStack()
    
    for char in reverse_string(input_string):
        reversed_stack.push(char)
        
    return reversed_stack


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print(type(reverse_stack(input_string)))