import numpy as np


def generate_random_walk(size: int) -> np.array:
    movements = np.random.normal(loc=0.0, scale=1.0, size=size)
    path = np.cumsum(movements)
    return path
