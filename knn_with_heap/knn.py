from math import sqrt
from collections import Counter
from knn_with_heap.heap import MinHeap

class KNN:
    def __init__(self, k=3):
        self.k = k
        self.data = []
    
    def fit(self, X, y):
        self.data = [(X[i], y[i]) for i in range(len(X))]
    
    def predict(self, X):
        predictions = []
        for point in X:
            heap = MinHeap()
            for data_point, label in self.data:
                distance = sqrt(sum((px - dx) ** 2 for px, dx in zip(point, data_point)))
                heap.insert((distance, label))
                if len(heap.heap) > self.k:
                    heap.delete_min()
            k_nearest = [heap.delete_min()[1] for _ in range(self.k)]
            predictions.append(Counter(k_nearest).most_common(1)[0][0])
        return predictions
