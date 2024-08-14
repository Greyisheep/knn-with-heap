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
                # Calculate Euclidean distance
                distance = sqrt(sum((px - dx) ** 2 for px, dx in zip(point, data_point)))
                # Insert (distance, label) into the heap
                heap.insert((distance, label))
                # Maintain only k elements in the heap (remove the largest distances)
                if len(heap.heap) > self.k:
                    heap.heap.sort(reverse=True)  # Ensure the largest distance is at the end
                    heap.heap.pop()  # Remove the largest distance
            
            # Collect the k nearest labels
            k_nearest = []
            while len(heap.heap) > 0:
                k_nearest.append(heap.delete_min()[1])
            
            # Debug: Print the k-nearest neighbors and distances
            print(f"K-nearest neighbors for point {point}: {k_nearest}")
            
            # Determine the most common label
            prediction = Counter(k_nearest).most_common(1)[0][0]
            predictions.append(prediction)
        return predictions
