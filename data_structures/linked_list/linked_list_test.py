from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
import unittest

class LinkedListTest(unittest.TestCase):

    def test_singly_linked_list(self):
        #empty linked list
        singlyLinkedList = SinglyLinkedList()
        self.assertEqual(0, len(singlyLinkedList))
        self.assertEqual([], list(singlyLinkedList))
        self.assertTrue(singlyLinkedList.is_empty())

        #adding one element
        singlyLinkedList.append(1)
        self.assertEqual(1, len(singlyLinkedList))
        self.assertEqual([1], list(singlyLinkedList))
        self.assertTrue(singlyLinkedList.contains(1))
        self.assertFalse(singlyLinkedList.contains(0))
        self.assertFalse(singlyLinkedList.is_empty())

        #prepend element test
        singlyLinkedList.prepend(3)
        singlyLinkedList.prepend(4)
        self.assertEqual(3, len(singlyLinkedList))
        self.assertEqual([4,3,1], list(singlyLinkedList))
        self.assertTrue(singlyLinkedList.contains(3))
        self.assertFalse(singlyLinkedList.contains(0))

        #append element test
        singlyLinkedList.append(2)
        self.assertEqual(4, len(singlyLinkedList))
        self.assertEqual([4,3,1,2], list(singlyLinkedList))
        self.assertTrue(singlyLinkedList.contains(2))
        self.assertFalse(singlyLinkedList.contains(0))

        #reverse linked list
        singlyLinkedList.reverse()
        self.assertEqual(4, len(singlyLinkedList))
        self.assertEqual([2,1,3,4], list(singlyLinkedList))

        #remove element not in list
        self.assertEqual(None, singlyLinkedList.remove(0))
        self.assertEqual(4, len(singlyLinkedList))
        self.assertEqual([2,1,3,4], list(singlyLinkedList))

        #remove middle element 
        self.assertEqual(1, singlyLinkedList.remove(1))
        self.assertEqual(3, len(singlyLinkedList))
        self.assertEqual([2,3,4], list(singlyLinkedList))

        #remove head element
        self.assertEqual(2, singlyLinkedList.remove_head())
        self.assertEqual(2, len(singlyLinkedList))
        self.assertEqual([3,4], list(singlyLinkedList))

        #remove tail element
        self.assertEqual(4, singlyLinkedList.remove_tail())
        self.assertEqual(1, len(singlyLinkedList))
        self.assertEqual([3], list(singlyLinkedList))

        #empty linked list and attempt removal on empty list
        self.assertEqual(3, singlyLinkedList.remove_head())
        self.assertEqual(0, len(singlyLinkedList))
        self.assertEqual(None, singlyLinkedList.remove_head())
        self.assertEqual(None, singlyLinkedList.remove_tail())
        self.assertEqual(None, singlyLinkedList.remove(1))
        self.assertEqual(0, len(singlyLinkedList))
        self.assertEqual([], list(singlyLinkedList))

    def test_doubly_linked_list(self):
        #empty linked list
        doublyLinkedList = DoublyLinkedList()
        self.assertEqual(0, len(doublyLinkedList))
        self.assertEqual([], list(doublyLinkedList))
        self.assertTrue(doublyLinkedList.is_empty())

        #adding one element
        doublyLinkedList.append(1)
        self.assertEqual(1, len(doublyLinkedList))
        self.assertEqual([1], list(doublyLinkedList))
        self.assertTrue(doublyLinkedList.contains(1))
        self.assertFalse(doublyLinkedList.contains(0))
        self.assertFalse(doublyLinkedList.is_empty())

        #prepend element test
        doublyLinkedList.prepend(3)
        doublyLinkedList.prepend(4)
        self.assertEqual(3, len(doublyLinkedList))
        self.assertEqual([4,3,1], list(doublyLinkedList))
        self.assertTrue(doublyLinkedList.contains(3))
        self.assertFalse(doublyLinkedList.contains(0))

        #append element test
        doublyLinkedList.append(2)
        self.assertEqual(4, len(doublyLinkedList))
        self.assertEqual([4,3,1,2], list(doublyLinkedList))
        self.assertTrue(doublyLinkedList.contains(2))
        self.assertFalse(doublyLinkedList.contains(0))

        #remove element not in list
        self.assertEqual(None, doublyLinkedList.remove(0))
        self.assertEqual(4, len(doublyLinkedList))
        self.assertEqual([4,3,1,2], list(doublyLinkedList))

        #remove middle element
        self.assertEqual(1, doublyLinkedList.remove(1))
        self.assertEqual(3, len(doublyLinkedList))
        self.assertEqual([4,3,2], list(doublyLinkedList))

        #remove head element
        self.assertEqual(4, doublyLinkedList.remove_head())
        self.assertEqual(2, len(doublyLinkedList))
        self.assertEqual([3,2], list(doublyLinkedList))

        #remove tail element
        self.assertEqual(2, doublyLinkedList.remove_tail())
        self.assertEqual(1, len(doublyLinkedList))
        self.assertEqual([3], list(doublyLinkedList))

        #empty linked list and attempt removal on empty list
        self.assertEqual(3, doublyLinkedList.remove_head())
        self.assertEqual(0, len(doublyLinkedList))
        self.assertEqual(None, doublyLinkedList.remove_head())
        self.assertEqual(None, doublyLinkedList.remove_tail())
        self.assertEqual(None, doublyLinkedList.remove(1))
        self.assertEqual(0, len(doublyLinkedList))
        self.assertEqual([], list(doublyLinkedList))

if __name__ == '__main__':
    unittest.main()