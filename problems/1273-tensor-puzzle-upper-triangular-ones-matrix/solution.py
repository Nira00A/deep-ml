import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    # Your code here
    arr = np.arange(n)
    return (arr[: , None] <= arr[None, :]).astype(np.float32)
