import unittest
from knn_with_heap.heap import MinHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def test_insert(self):
        self.heap.insert(10)
        self.assertEqual(self.heap.peek_min(), 10)

    def test_delete_min(self):
        self.heap.insert(10)
        self.heap.insert(5)
        self.heap.insert(15)
        self.assertEqual(self.heap.delete_min(), 5)
        self.assertEqual(self.heap.peek_min(), 10)

    def test_peek_min(self):
        self.heap.insert(10)
        self.assertEqual(self.heap.peek_min(), 10)
        self.heap.insert(5)
        self.assertEqual(self.heap.peek_min(), 5)

if __name__ == '__main__':
    unittest.main()
