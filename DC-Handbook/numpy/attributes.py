import numpy as np

rng = np.random.default_rng(seed=1701)

x1  = rng.integers(10, size=6)
x2  = rng.integers(10, size=(3, 4))
x3  = rng.integers(10, size=(3, 4, 5))

print('x3 ndim:', x3.ndim)
print('x3 shape:', x3.shape)
print('x3 size:', x3.size)
print('x3 dtype:', x3.dtype)

