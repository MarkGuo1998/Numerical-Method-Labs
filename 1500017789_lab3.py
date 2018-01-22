import numpy as np

n = 5

A = [[5,-1,0,0,0],[-1,4.5,0.2,0,0],[0,0.2,1,-0.4,0],[0,0,-0.4,3,1],[0,0,0,1,3]]
A = np.array(A)


for j in range(n):
    for k in range(j):
        P = np.identity(n)
        if A[j][j] != A[k][k]:
            c = 2 * A[j][k] * np.sign(A[j][j] - A[k][k])
            b = np.abs(A[j][j] - A[k][k])
            P[j][j] = np.sqrt(0.5 * (1 + b / np.sqrt(c ** 2 + b ** 2)))
            P[k][k] = P[j][j]
            P[k][j] = -c / (2 * P[j][j] * np.sqrt(c ** 2 + b ** 2))
            P[j][k] = -P[k][j]
        else:
            P[j][j] = 1 / np.sqrt(2)
            P[k][k] = P[j][j]
            P[k][j] = P[j][j]
            P[j][k] = -P[j][j]
        A = np.dot(np.dot(P, A), np.transpose(P))
        print(A)

print(A)

# another method reference @ https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm
# import numpy as np
#
# n = 5
#
# A = [[5,-1,0,0,0],[-1,4.5,0.2,0,0],[0,0.2,1,-0.4,0],[0,0,-0.4,3,1],[0,0,0,1,3]]
# A = np.array(A)
#
#
# for j in range(n):
#     for k in range(j):
#         P = np.identity(n)
#         if A[j][j] != A[k][k]:
#             theta = np.arctan(2 * A[j][k] / (A[k][k] - A[j][j])) / 2
#             P[j][j] = np.cos(theta)
#             P[k][k] = P[j][j]
#             P[j][k] = -np.sin(theta)
#             P[k][j] = -P[j][k]
#         else:
#             P[j][j] = 1 / np.sqrt(2)
#             P[k][k] = P[j][j]
#             P[k][j] = P[j][j]
#             P[j][k] = -P[j][j]
#         A = np.dot(np.dot(P, A), np.transpose(P))
#         print(A)
#
# print(A)