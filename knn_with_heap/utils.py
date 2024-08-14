import csv

def load_dataset(filename):
    data = []
    labels = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if len(row) < 5:  # Expecting 4 features and 1 label
                continue  # Skip rows that don't have enough columns
            data.append([float(x) for x in row[:-1]])
            labels.append(row[-1])
    return data, labels
