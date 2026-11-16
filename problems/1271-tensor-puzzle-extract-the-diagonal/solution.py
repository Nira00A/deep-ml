import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    # Your code here

    idx = np.arange(min(A.shape))
    return np.array(A[idx,idx])