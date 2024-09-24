import numpy as np

l = [[1,0,0],[0,1,0],[0,0,1]]

x = [np.array([d,
             [-90,160,0],
             [315,-240,195]]) for d in l]
print(np.linalg.det(x[0]), np.linalg.det(x[1]), np.linalg.det(x[2]))