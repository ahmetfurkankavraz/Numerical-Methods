# Ahmet Furkan Kavraz
# 150190024
# This contains only the code of the program.
# For the result of part-b please look pdf.

import numpy as np 

# The initial vector which is using for power method iteration
vector1 = np.array([1, 2,-1])
vector2 = np.array([1, 2, 1])
# Original matrix A
matrix_A = np.array([[-2, 1, 4], [1, 1, 1], [4, 1,-2]])

eigenvalue1 = 0
eigenvalue2 = 0

for k in range(0, 5):
    # Steps of the power method
    vector1 = np.dot(matrix_A, vector1)
    vector2 = np.dot(matrix_A, vector2)

    vector1_norm = np.linalg.norm(vector1)
    vector2_norm = np.linalg.norm(vector2)

    vector1 = vector1 / vector1_norm
    vector2 = vector2 / vector2_norm

    eigenvalue1 = np.matmul(np.matmul(np.transpose(vector1), matrix_A), vector1)
    eigenvalue2 = np.matmul(np.matmul(np.transpose(vector2), matrix_A), vector2)

    # Printing necessary information about Eigenvalue iteration
    print("Iteration number", k )
    print("Eigenvalue1: ", eigenvalue1 )
    print("Eigenvector1: ", vector1 )
    print("Eigenvalue2: ", eigenvalue2 )
    print("Eigenvector2: ", vector2 )
    print("")

# Printing the reel values of eigenvalue and eigenvector
results = np.linalg.eig(matrix_A)

print("Real eigenvalue matrix: ")
print(results[0])
print("Real eigenvector matrix: ")
print(results[1])