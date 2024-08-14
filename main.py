from knn_with_heap.utils import load_dataset
from knn_with_heap.knn import KNN

# Load the dataset
X, y = load_dataset('data/iris.csv')

# Initialize KNN with k=3
knn = KNN(k=3)

# Fit the model
knn.fit(X, y)

# Predict a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = knn.predict(sample)

print(f'The predicted class for the sample {sample} is {prediction}')
