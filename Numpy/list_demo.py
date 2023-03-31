import random

import numpy as np

ar=np.array([[10,20,30,40],[1,2,3,4]])
ar2=np.array([1,3])
# print(ar.ndim)
# print(np.zeros((3,3)))
# print(np.ones((2,2)))
# print(np.identity(3))
# print(np.eye(4,k=2))
# print(np.sin(ar2))
# print(np.cos(ar2))
# print(np.log2(ar2))
print(np.linalg.solve(ar,ar2))
# print(np.random.randint(1,10,4))
# ar3=ar2+2
# print(ar3)
# print(type(ar))
