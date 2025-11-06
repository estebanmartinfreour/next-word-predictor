import numpy as np


def create_training_sequences(list, window):
    "The aim of this function is to create a dataset which contained 2 numpy arrays : 1 which is composed of the previous word in the window"
    "just before a word, and another numpy aray composed of those words which we called the targets of our model."
    n = len(list)
    n_inputs = n-window
    X = np.full((n_inputs, window), -1)
    y = np.arange(n_inputs)
    for i in range(n_inputs):
        X[i] = list[i:(i+window)]
        y[i] = list[i+window]
    return X, y

print(create_training_sequences([1, 2, 3, 4, 5, 6, 7, 1, 2, 3], 3))