import numpy as np
from scipy import linalg


#a) Define a matrix A
A = np.array([[1, -2, 3],
              [4, 5, 6],
              [7, 1, 9]])
print(A)
#b) Define a vector b
b = np.arange(1, 4)
print(b)
#c) Solve the linear system of equations A x = b
x = linalg.solve(A, b)
print(x)
#d) Check that your solution is correct by plugging it into the equation
A.dot(x.T)

#e) Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)

B = np.random.rand(9).reshape(3, 3)
print(B)

# Solve for x
X = linalg.solve(A, B)


#f. Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
eigen_val=linalg.eigvals(A)
print(eigen_val)

#g. Calculate the inverse, determinant of A
A_inv = np.linalg.inv(A)
print(A_inv)

from scipy.linalg import det
print(det(A))

#h. Calculate the norm of A with different orders

from numpy.linalg import norm

# Calculate norms of A for different orders
norm_fro = norm(A, ord='fro')  # Frobenius norm
norm_1 = norm(A, ord=1)  # 1-norm (max column sum)
norm_2 = norm(A, ord=2)  # 2-norm (largest singular value)
norm_inf = norm(A, ord=np.inf)  # Infinity norm (max row sum)

print("Frobenius norm of A:", norm_fro)
print("1-norm of A:", norm_1)
print("2-norm of A:", norm_2)
print("Infinity norm of A:", norm_inf)


