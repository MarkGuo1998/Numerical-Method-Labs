import numpy as np

def f(y,t):
    return y/t-(y/t)**2


a = float(input("a = "))
b = float(input("b = "))
alpha = float(input("alpha = "))
tol = float(input("TOL = "))
hmin = float(input("hmin = "))
hmax = float(input("hmax = "))

# step 1
t = alpha
w = alpha
h = hmax
flag = 1

# step 2
while (flag == 1):
    print("h = %f" %h)
    # step 3
    K1 = h * f(t, w)
    K2 = h * f(t + h / 6.0, w + (1 / 6.0) * K1)
    K3 = h * f(t + (4 / 15.0) * h, w + (4 / 75.0) * K1 + (16 / 75.0) * K2)
    K4 = h * f(t + (2 / 3.0) * h, w + (5 / 6.0) * K1 - (8 / 3.0) * K2 + (5 / 2.0) * K3)
    K5 = h * f(t + (5 / 6.0) * h, w - (165 / 64.0) * K1 + (55 / 6.0) * K2 - (425 / 64.0) * K3 + (85 / 96.0) * K4)
    K6 = h * f(t + h, w + (12 / 5.0) * K1 - (8) * K2 + (4015 / 612.0) * K3 - (11 / 36.0) * K4 + (88 / 255.0) * K5)
    K7 = h * f(t + h / 15.0, w - (8263 / 15000.0) * K1 + (124 / 75.0) * K2 - (643 / 680.0) * K3 - (81 / 250.0) * K4 + (2484 / 10625.0) * K5)
    K8 = h * f(t + h, w + (3051 / 1720.0) * K1 - (300 / 43.0) * K2 + (297275 / 52632.0) * K3 - (319 / 2322.0) * K4 + (24608 / 80645.0) * K5 + (3850 / 26703.0) * K7)

    # step 4
    wip1 = w + (13 / 160.0) * K1 + (2375 / 5984.0) * K3 + (5 / 16.0) * K4 + (12 / 85.0) * K5 + (3 / 44.0) * K6  # 'p' for '+'
    wip1_ = w + (3 / 40.0) * K1 + (875 / 2244.0) * K3 + (23 / 72.0) * K4 + (264 / 1955.0) * K5 + (125 / 11592.0) * K7 + (43 / 616.0) * K8  # '_' for '~'
    R = abs(wip1_ - wip1) / h
    print("R = %f" %R)

    # step 5-7
    if R <= tol:
        t = t + h
        w = wip1
        print("t = %f, w = %f" %(t, w))

    # step 8
    delta = 0.87*(tol/R)**(1/5)

    # step 9
    if delta <= 0.1:
        h = 0.1 * h
    elif delta >= 4:
        h = 4 * h
    else:
        h = delta * h

    # step 10
    if h > hmax:
        h = hmax

    # step 11
    if t >= b:
        flag = 0
    elif t + h > b:
        h = b - t
    elif h < hmin:
        flag = 0
        print("minimum h exceeded, fail.")
        break

# step 12
if flag == 1:
    print("success.")