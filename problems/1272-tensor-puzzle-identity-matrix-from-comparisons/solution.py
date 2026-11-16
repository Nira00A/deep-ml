import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    # Your code here
    arr = np.arange(n)

    return (arr[:,None] == arr[None,:]).astype(float)
