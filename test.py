import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 10
u = 10.0

def calculate_r(t, theta, u, g):
    theta_rad = np.radians(theta)
    r = np.sqrt((u**2 * t**2) - (g* t**3 * u * np.sin(theta_rad)) + (1/4 * (g**2) * (t**4)))
    return r

def calculate_xy(t, theta, u, g):
    theta_rad = np.radians(theta)
    x = u * t * np.cos(theta_rad)
    y = u * t * np.sin(theta_rad) - 0.5 * g * t**2
    return x, y

thetas = [30, 45, 60, 70.5, 78, 85]
time_values = np.arange(0.1, 5.1, 0.1)

for max_time in time_values:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    t = np.linspace(0, max_time, 1000)
    
    for theta in thetas:
        r = calculate_r(t, theta, u, g)
        x, y = calculate_xy(t, theta, u, g)
        ax1.plot(t, r, label=f'θ = {theta}°')
        ax2.plot(x, y, label=f'θ = {theta}°')
    
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Range (m)')
    ax1.set_title('Range vs Time')
    ax1.legend()

    ax2.set_xlabel('Distance (m)')
    ax2.set_ylabel('Height (m)')
    ax2.set_title('Height vs Distance')
    ax2.legend()

    plt.savefig(f'plots/plot_{int(max_time*10)}.png')
    plt.close(fig)
