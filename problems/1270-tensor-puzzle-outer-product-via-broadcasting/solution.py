import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Outer product of 1-D arrays a and b via broadcasting."""
    # Your code here
    return np.dot(a[: , None], b[None , :])
