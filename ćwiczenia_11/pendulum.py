import numpy as np
import matplotlib.pyplot as plt
import sys
g = 9.81

# Przykład wywołania: python3 pendulum.py 1 0.1 0.0 10 0.01 --RK4

def pendulum_euler(l, theta0, omega0, tmax, dt):
    '''https://en.wikipedia.org/wiki/Euler_method'''
    t = np.arange(0, tmax, dt)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, len(t)):
        omega[i] = omega[i-1] - (g / l) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i-1] * dt

    return t, theta, omega

def pendulum_midpoint(l, theta0, omega0, tmax, dt):
    '''https://en.wikipedia.org/wiki/Midpoint_method'''
    t = np.arange(0, tmax, dt)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, len(t)):
        omega_half = omega[i-1] - (g / l) * np.sin(theta[i-1]) * dt / 2
        theta_half = theta[i-1] + omega[i-1] * dt / 2
        omega[i] = omega[i-1] - (g / l) * np.sin(theta_half) * dt
        theta[i] = theta[i-1] + omega_half * dt

    return t, theta, omega

def pendulum_rk4(l, theta0, omega0, tmax, dt):
    '''https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods'''
    t = np.arange(0, tmax, dt)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    theta[0] = theta0
    omega[0] = omega0

    for i in range(1, len(t)):
        k1_theta = omega[i-1]
        k1_omega = -(g / l) * np.sin(theta[i-1])

        k2_theta = omega[i-1] + k1_omega * dt / 2
        k2_omega = -(g / l) * np.sin(theta[i-1] + k1_theta * dt / 2)

        k3_theta = omega[i-1] + k2_omega * dt / 2
        k3_omega = -(g / l) * np.sin(theta[i-1] + k2_theta * dt / 2)

        k4_theta = omega[i-1] + k3_omega * dt
        k4_omega = -(g / l) * np.sin(theta[i-1] + k3_theta * dt)

        theta[i] = theta[i-1] + (dt / 6) * (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta)
        omega[i] = omega[i-1] + (dt / 6) * (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega)

    return t, theta, omega


l = float(sys.argv[1])
theta0 = float(sys.argv[2])
omega0 = float(sys.argv[3])
tmax = float(sys.argv[4])
dt = float(sys.argv[5])
method = sys.argv[6] if len(sys.argv) > 6 else "--RK4"

# Wybór metody
if method == "--Euler": # warto zauważyć że dla metody Eulera nie jest zachowana energia wahadła
    t, theta, omega = pendulum_euler(l, theta0, omega0, tmax, dt)
elif method == "--midpoint":
    t, theta, omega = pendulum_midpoint(l, theta0, omega0, tmax, dt)
elif method == "--RK4":
    t, theta, omega = pendulum_rk4(l, theta0, omega0, tmax, dt)

# Rysowanie wykresów
plt.plot(t, theta, label="theta")
plt.plot(t, omega, label="omega")
plt.xlabel("t")
plt.legend()
plt.show()

plt.plot(theta, omega)
plt.xlabel("theta")
plt.ylabel("omega")
plt.show()