import numpy as np

A = np.array(list(range(25))).reshape((5,5))
A = np.random.rand(25).reshape((5,5))
x = np.array(list(range(5)))

b = A.dot(A)

det = np.linalg.det(A)

