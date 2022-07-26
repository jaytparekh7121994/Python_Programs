from unittest import TestCase
from stack import Stack 


class StackTestCases(TestCase):
    """ Test Cases to test stack functionality """

    def setUp(self) -> None:
        self.stack = Stack()

    def tearDown(self) -> None:
        self.stack = None

    def test_push(self):
        """ Test pushing an item in stack """
        self.stack.push(9)
        self.assertEqual(self.stack.peek(), 9)

    def test_pop(self):
        """ Test popping or removing an item from stack """
        self.stack.push(9)
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())

    def test_peek(self):
        """ Test peek into the last item of stack """
        self.stack.push(8)
        self.stack.push(9)
        self.assertTrue(self.stack.peek(), 9)

    def test_isEmpty(self):
        """ Test if the stack is empty """
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(5)
        self.assertFalse(self.stack.isEmpty())
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())