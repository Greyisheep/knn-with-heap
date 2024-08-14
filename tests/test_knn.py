import unittest
from knn_with_heap.knn import KNN
from knn_with_heap.utils import load_dataset

class TestKNN(unittest.TestCase):
    def setUp(self):
        self.knn = KNN(k=3)
        X, y = load_dataset('data/iris.csv')
        self.knn.fit(X, y)

    def test_predict(self):
        prediction = self.knn.predict([[5.1, 3.5, 1.4, 0.2]])
        self.assertEqual(prediction, ['Iris-setosa'])

if __name__ == '__main__':
    unittest.main()
