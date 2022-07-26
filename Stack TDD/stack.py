"""Implements Stack functionality"""
from typing import Any


class Stack:
    """Stack functionality """

    def __init__(self):
        """ Constructor """
        self.items = []
       
    def push(self, data: Any) -> None:
        """ Push new item to stack """
        self.items.append(data)
   
    def pop(self) -> Any:
        """ Removes the latest object from stack """
        self.items.pop()
   
    def peek(self) -> Any:
        """ Returns the latest object from stack """
        return self.items[-1]
   
    def isEmpty(self) -> bool:
        """Returns true if the stack is empty """
        return len(self.items) == 0
