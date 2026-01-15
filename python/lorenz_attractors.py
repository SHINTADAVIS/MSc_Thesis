import numpy as np
import matplotlib.pyplot as plt

# Lorenz-model equations for laser system
def f(t, x, y, z):
    return -10 * (x - y)

def g(t, x, y, z, r):
    return -y - x * z + r * x

def w(t, x, y, z):
    return x * y - 2.66 * z

# Get control parameter
r = float(input("Enter the value of r: "))

# Runge–Kutta 4th order solver
def solution(t0, x0, y0, z0, h, n, r):
    t, x, y, z = t0, x0, y0, z0

    for i in range(n):
        k1 = h * f(t, x, y, z)
        l1 = h * g(t, x, y, z, r)
        m1 = h * w(t, x, y, z)

        k2 = h * f(t + h/2, x + k1/2, y + l1/2, z + m1/2)
        l2 = h * g(t + h/2, x + k1/2, y + l1/2, z + m1/2, r)
        m2 = h * w(t + h/2, x + k1/2, y + l1/2, z + m1/2)

        k3 = h * f(t + h/2, x + k2/2, y + l2/2, z + m2/2)
        l3 = h * g(t + h/2, x + k2/2, y + l2/2, z + m2/2, r)
        m3 = h * w(t + h/2, x + k2/2, y + l2/2, z + m2/2)

        k4 = h * f(t + h, x + k3, y + l3, z + m3)
        l4 = h * g(t + h, x + k3, y + l3, z + m3, r)
        m4 = h * w(t + h, x + k3, y + l3, z + m3)

        t += h
        x += (k1 + 2*k2 + 2*k3 + k4) / 6
        y += (l1 + 2*l2 + 2*l3 + l4) / 6
        z += (m1 + 2*m2 + 2*m3 + m4) / 6

        plt.figure(1)
        plt.plot(t, x, '.')
        plt.xlabel('t')
        plt.ylabel('x')
        plt.title('x–t graph')

        plt.figure(2)
        plt.plot(t, y, '.')
        plt.xlabel('t')
        plt.ylabel('y')
        plt.title('y–t graph')

        plt.figure(3)
        plt.plot(t, z, '.')
        plt.xlabel('t')
        plt.ylabel('z')
        plt.title('z–t graph')

        plt.figure(4)
        plt.plot(x, z, '.')
        plt.xlabel('x')
        plt.ylabel('z')
        plt.title('x–z attractor')

        plt.figure(5)
        plt.plot(x, y, '.')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('x–y attractor')

        plt.figure(6)
        plt.plot(y, z, '.')
        plt.xlabel('y')
        plt.ylabel('z')
        plt.title('y–z attractor')

    return x, y, z

# Run simulation
solution(0, 0, 0, 0, 0.01, 3500, r)
plt.show()
