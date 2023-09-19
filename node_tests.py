import unittest

from LinkedListNode import LinkedListNode


class TestNodes(unittest.TestCase):
    def test_nodes(self):
        node= LinkedListNode(10)
        self.assertEqual(node.data,10)