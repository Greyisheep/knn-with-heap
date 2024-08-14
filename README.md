# KNN with Min-Heap

This project implements a Min-Heap data structure and uses it to build a K-Nearest Neighbors (KNN) algorithm. The KNN algorithm is applied to the Iris dataset to classify species of iris flowers.

## Project Structure

- `knn_with_heap/`: Contains the implementation of the Min-Heap and KNN algorithm.
- `data/`: Contains the dataset (Iris dataset).
- `tests/`: Contains unit tests for the Min-Heap and KNN.
- `main.py`: Example script to run the KNN on the Iris dataset.

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Usage

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/knn_with_heap.git
    cd knn_with_heap
    ```

2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the example:
    ```
    python main.py
    ```

4. Run the tests:
    ```
    python -m unittest discover tests/
    ```

## References

- [Min-Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))
- [K-Nearest Neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
