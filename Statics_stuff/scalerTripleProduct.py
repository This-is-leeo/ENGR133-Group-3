import numpy as np
from math import sqrt

def scalar_triple_product(A, B, C):
    cross_product = np.cross(B, C)
    scalar_triple = np.dot(A, cross_product)
    
    return scalar_triple

# A = np.array(list(map(float, input("Enter the components of vector A separated by spaces: ").split())))
# B = np.array(list(map(float, input("Enter the components of vector B separated by spaces: ").split())))
# C = np.array(list(map(float, input("Enter the components of vector C separated by spaces: ").split())))

A = np.array([0, 1/sqrt(2) , 1/sqrt(2)])
B = np.array([1,1,0])
C = np.array([0, -2/sqrt(2), 2  /sqrt(2)])

result = scalar_triple_product(A, B, C)

print(f"The scalar triple product is: {result}")
