import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import mpld3

def calculate_trajectory(theta, g, u, h, delta_t):
    theta_rad = np.radians(theta)
    t_max = (u * np.sin(theta_rad) + np.sqrt((u * np.sin(theta_rad))**2 + 2 * g * h)) / g
    t = np.arange(0, t_max + delta_t, delta_t)
    x = u * np.cos(theta_rad) * t
    y = h + u * np.sin(theta_rad) * t - 0.5 * g * t**2
    return x, y

theta_init = 45
g_init = 9.81
u_init = 20.0
h_init = 0.0
delta_t_init = 0.01

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
x, y = calculate_trajectory(theta_init, g_init, u_init, h_init, delta_t_init)
line, = plt.plot(x, y, lw=2)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Task 1')

ax.set_xlim(0, 100)
ax.set_ylim(0, 50)

axcolor = 'lightgoldenrodyellow'
ax_theta = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_u = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_h = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_dt = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor=axcolor)

s_theta = Slider(ax_theta, 'Angle (deg)', 0, 90, valinit=theta_init)
s_u = Slider(ax_u, 'Speed (m/s)', 0, 100, valinit=u_init)
s_h = Slider(ax_h, 'Height (m)', 0, 100, valinit=h_init)
s_dt = Slider(ax_dt, 'Delta t (s)', 0.001, 1, valinit=delta_t_init)

def update(val):
    theta = s_theta.val
    u = s_u.val
    h = s_h.val
    delta_t = s_dt.val
    x, y = calculate_trajectory(theta, g_init, u, h, delta_t)
    line.set_xdata(x)
    line.set_ydata(y)
    fig.canvas.draw_idle()

s_theta.on_changed(update)
s_u.on_changed(update)
s_h.on_changed(update)
s_dt.on_changed(update)

plt.show()
html_str = mpld3.fig_to_html(fig)
Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()