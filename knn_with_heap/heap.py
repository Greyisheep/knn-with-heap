"""
A MinHeap implementation for storing elements as tuples (priority, value).
"""

class MinHeap:
    """
    MinHeap class for efficient priority queue operations.
    """

    def __init__(self):
        """
        Initializes an empty MinHeap.
        """
        self.heap = []

    def insert(self, element):
        """
        Inserts an element into the MinHeap.

        Args:
            element: A tuple (priority, value) to be inserted.
        """
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def delete_min(self):
        """
        Removes and returns the minimum element from the MinHeap.

        Returns:
            The minimum element (tuple) or None if the heap is empty.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_element

    def _heapify_up(self, index):
        """
        Maintains the heap property by moving an element up the heap.

        Args:
            index: The index of the element to be heapified up.
        """
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """
        Maintains the heap property by moving an element down the heap.

        Args:
            index: The index of the element to be heapified down.
        """
        n = len(self.heap)
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < n and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child

        if right_child < n and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
