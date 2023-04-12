import numpy as np

kernel_5x5 = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
])

print(kernel_5x5 / np.sum(kernel_5x5))
print(np.reshape(kernel_5x5, (1, 25)) == np.ravel(kernel_5x5))
