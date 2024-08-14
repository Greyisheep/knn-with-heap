"""
K-Nearest Neighbors (KNN) classifier using a MinHeap for efficient distance calculations.
"""

from math import sqrt
from collections import Counter
from knn_with_heap.heap import MinHeap

class KNN:
    """
    KNN classifier.

    Args:
        k (int, optional): Number of neighbors to consider. Defaults to 3.
    """

    def __init__(self, k=3):
        self.k = k
        self.data = []

    def fit(self, X, y):
        """
        Fits the KNN model to the training data.

        Args:
            X: Feature matrix of shape (n_samples, n_features).
            y: Target labels of shape (n_samples,).
        """
        self.data = [(X[i], y[i]) for i in range(len(X))]

    def predict(self, X):
        """
        Predicts the class labels for the given test data.

        Args:
            X: Feature matrix of shape (n_samples, n_features).

        Returns:
            Predicted class labels for the test data.
        """
        predictions = []
        for point in X:
            heap = MinHeap()
            for i, (data_point, label) in enumerate(self.data):
                distance = sqrt(sum((px - dx) ** 2 for px, dx in zip(point, data_point)))
                if len(heap.heap) < self.k:
                    heap.insert((distance, label))
                else:
                    if distance < heap.heap[0][0]:
                        heap.delete_min()
                        heap.insert((distance, label))

            k_nearest = [label for _, label in heap.heap]
            prediction = Counter(k_nearest).most_common(1)[0][0]
            predictions.append(prediction)
        return predictions
