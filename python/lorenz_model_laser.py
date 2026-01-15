import numpy as np
import matplotlib.pyplot as plt

# Lorenz-model like equations for laser dynamics
def f(t, x, y, z):
    return -10 * (x - y)

def g(t, x, y, z, r):
    return -y - x * z - r * x

def w(t, x, y, z):
    return x * y - 5 * z

# 4th order Runge-Kutta solver
def solution(t0, x0, y0, z0, h, n):
    t, x, y, z = t0, x0, y0, z0

    t_list, x_list, y_list, z_list, r_list = [], [], [], [], []
    r_values = np.linspace(-400, 400, n)

    for r in r_values:
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

        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        r_list.append(r)

    return t_list, x_list, y_list, z_list, r_list


# Run simulation
t, x, y, z, r = solution(t0=0, x0=1, y0=1, z0=1, h=0.005, n=500)

# Plot results
plt.figure()
plt.plot(t, x)
plt.xlabel("Time")
plt.ylabel("X")
plt.title("X vs Time")

plt.figure()
plt.plot(t, y)
plt.xlabel("Time")
plt.ylabel("Y")
plt.title("Y vs Time")

plt.figure()
plt.plot(t, z)
plt.xlabel("Time")
plt.ylabel("Z")
plt.title("Z vs Time")

plt.figure()
plt.plot(r, x)
plt.xlabel("Parameter r")
plt.ylabel("X")
plt.title("Bifurcation-like Plot")

plt.show()
