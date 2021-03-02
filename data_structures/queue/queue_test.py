from list_queue import ListQueue
from node_queue import NodeQueue
from stack_queue import StackQueue
import unittest

class StackTest(unittest.TestCase):

    def test_list_queue(self):
        list_queue = ListQueue()
        self.assertEqual(0, len(list_queue))

        #Dequeue from empty list
        self.assertEqual(None, list_queue.dequeue())

        #Enqueue test
        list_queue.enqueue(1)
        list_queue.enqueue(2)
        list_queue.enqueue(3)
        self.assertEqual(3, len(list_queue))

        #Dequeue until empty
        self.assertEqual(1, list_queue.dequeue())
        self.assertEqual(2, len(list_queue))
        self.assertEqual(2, list_queue.dequeue())
        self.assertEqual(1, len(list_queue))
        self.assertEqual(3, list_queue.dequeue())
        self.assertEqual(0, len(list_queue))
        self.assertEqual(None, list_queue.dequeue())
        self.assertEqual(0, len(list_queue))

    def test_node_queue(self):
        stack_queue = StackQueue()
        self.assertEqual(0, len(stack_queue))

        #Dequeue from empty list
        self.assertEqual(None, stack_queue.dequeue())

        #Enqueue test
        stack_queue.enqueue(1)
        stack_queue.enqueue(2)
        stack_queue.enqueue(3)
        self.assertEqual(3, len(stack_queue))

        #Dequeue until empty
        self.assertEqual(1, stack_queue.dequeue())
        self.assertEqual(2, len(stack_queue))
        self.assertEqual(2, stack_queue.dequeue())
        self.assertEqual(1, len(stack_queue))
        self.assertEqual(3, stack_queue.dequeue())
        self.assertEqual(0, len(stack_queue))
        self.assertEqual(None, stack_queue.dequeue())
        self.assertEqual(0, len(stack_queue))

    def test_stack_queue(self):
        node_queue = NodeQueue()
        self.assertEqual(0, len(node_queue))

        #Dequeue from empty list
        self.assertEqual(None, node_queue.dequeue())

        #Enqueue test
        node_queue.enqueue(1)
        node_queue.enqueue(2)
        node_queue.enqueue(3)
        self.assertEqual(3, len(node_queue))

        #Dequeue until empty
        self.assertEqual(1, node_queue.dequeue())
        self.assertEqual(2, len(node_queue))
        self.assertEqual(2, node_queue.dequeue())
        self.assertEqual(1, len(node_queue))
        self.assertEqual(3, node_queue.dequeue())
        self.assertEqual(0, len(node_queue))
        self.assertEqual(None, node_queue.dequeue())
        self.assertEqual(0, len(node_queue))

if __name__ == '__main__':
    unittest.main()