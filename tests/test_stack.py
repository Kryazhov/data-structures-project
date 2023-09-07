import unittest
from src.stack import Stack

class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertIsNone(self.stack.top)

        self.stack.push(1)
        self.assertEqual(self.stack.top.data, 1)
        self.assertIsNone(self.stack.top.next_node)

        self.stack.push(2)
        self.assertEqual(self.stack.top.data, 2)
        self.assertEqual(self.stack.top.next_node.data, 1)
