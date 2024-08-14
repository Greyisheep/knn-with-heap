"""
Utility functions for loading datasets.
"""

import csv

def load_dataset(filename):
    """
    Loads a dataset from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        A tuple containing the data and labels.
    """
    data = []
    labels = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if len(row) < 5:
                continue  # Skip rows that don't have enough columns
            data.append([float(x) for x in row[:-1]])
            labels.append(row[-1])
    return data, labels
