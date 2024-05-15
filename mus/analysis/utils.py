import numpy as np


def generate_random_seeds(n: int) -> list[int]:
    rng = np.random.default_rng()
    return rng.integers(1000000, size=(n,)).tolist()
