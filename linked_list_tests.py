import unittest

from LinkedList import LinkedList
from LinkedListNode import LinkedListNode

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linkedList = LinkedList()
        self.linkedList.add(LinkedListNode(10))
    def test_adding_is_successful(self):
        self.assertEqual(self.linkedList.length,1)

    def test_adding_to_linked_list(self):
        self.linkedList.add(LinkedListNode(20))
        self.assertEqual(self.linkedList.length,2)

    def test_adding_duplicates_should_not_add_to_the_length(self):
        self.linkedList.add(LinkedListNode(20))
        self.linkedList.add(LinkedListNode(20))
        self.assertEqual(self.linkedList.length,3)

    def test_adding_node_on_the_front(self):
        self.linkedList.add_head(LinkedListNode(22))
        self.assertEqual(self.linkedList.head.data,22)

    def test_search_for_node(self):
        self.linkedList.add(LinkedListNode(20))
        self.linkedList.add(LinkedListNode(30))
        self.assertEqual(self.linkedList.search(30).data,30)
        self.assertEqual(self.linkedList.search(20).data,20)

    def test_search_for_non_existent_node(self):
        self.linkedList.add(LinkedListNode(20))
        self.linkedList.add(LinkedListNode(30))
        self.assertEqual(self.linkedList.search(40),None)
