from unittest import TestCase
from stack import Stack 


class StackTestCases(TestCase):
    """ Test Cases to test stack functionality """

    def setUp(self) -> None:
        self.stack = Stack()

    def tearDown(self) -> None:
        self.stack = None

    def test_push(self):
        self.stack.push(9)
        self.assertEqual(self.stack.peek(), 9)

    def test_pop(self):
        self.stack.push(9)
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())

    