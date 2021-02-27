from stack import Stack
import unittest

class StackTest(unittest.TestCase):

    def test_stack(self):
        #empty stack test
        stack = Stack()
        self.assertEqual(0, len(stack))
        self.assertEqual(None, stack.pop())
        self.assertEqual(None, stack.peek())

        #push to stack
        stack.push(1)
        self.assertEqual(1, len(stack))
        self.assertEqual(1, stack.peek())

        stack.push(3)
        self.assertEqual(2, len(stack))
        self.assertEqual(3, stack.peek())

        #pop from stack
        self.assertEqual(3, stack.pop())
        self.assertEqual(1, len(stack))
  
        #pop from stack
        self.assertEqual(1, stack.pop())
        self.assertEqual(0, len(stack))

if __name__ == '__main__':
    unittest.main()