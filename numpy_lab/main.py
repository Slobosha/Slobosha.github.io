import numpy as np

def create_vector() -> np.ndarray:
    """Создать массив от 0 до 9."""
    return np.arange(10)

def create_matrix() -> np.ndarray:
    """Создать матрицу 5x5 со случайными числами от 0 до 1."""
    return np.random.rand(5, 5)

def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """Преобразовать массив формы (10,) в форму (2,5)."""
    return vec.reshape(2, 5)

def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """Транспонировать входную матрицу."""
    return mat.T
