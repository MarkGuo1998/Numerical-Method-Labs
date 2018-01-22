import numpy as np

A = np.zeros(shape = [80, 80])

for i in range(80):
    A[i][i] = 2 * (i+1)

for i in range(78):
    A[i][i+2] = 0.5 * (i+1)
    A[i+2][i] = 0.5 * (i+3)

for i in range(76):
    A[i][i+4] = 0.25 * (i+1)
    A[i+4][i] = 0.25 * (i+5)

b = np.pi*np.ones(shape=80)

tol = float(input("tol = "))
N = int(input("Max_iters = "))
w = float(input("param w = "))
xo = x = np.zeros(shape=80)
flag = False

for k in range(N):
    x = np.zeros(shape=80)
    for i in range(80):
        x[i] = (1 - w) * xo[i] + w * b[i] / A[i][i]
        for j in range(i):
            x[i] = x[i] - w * x[j] * A[i][j] / A[i][i]
        for j in range(i + 1, 80):
            x[i] = x[i] - w * xo[j] * A[i][j] / A[i][i]
    if np.max(np.abs(x - xo)) < tol:
        print("Succeed, x = ", x)
        print("Ax - b = ", np.dot(A,x)-b)
        flag = True
        break
    xo = x

if flag == False:
    print("Fail")

