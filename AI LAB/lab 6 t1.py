
import numpy as np

# Task 1: Convert all elements of a numpy array from float to Bool
a = np.array([[1.5, 0.0, 3.2], [4.1, 0.0, 2.3]], dtype=float)
bool_array = a.astype(bool)
print("Task 1 - Bool Array:")
print(bool_array)