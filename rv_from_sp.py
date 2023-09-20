import matplotlib.pyplot as plt
import numpy as np
from fig_style_config import figure_size, font_size, label_font_size, legend_font_size, line_width

# Set Matplotlib style parameters
plt.rcParams.update({
    'font.size': font_size,
    'lines.linewidth': line_width,
    'figure.figsize': figure_size,
    'legend.fontsize': legend_font_size,
    'xtick.labelsize': label_font_size,
    'ytick.labelsize': label_font_size,
    'axes.labelsize': label_font_size
})

seed_value = 40
np.random.seed(seed_value)
# Set parameters
num_trajectories = 200
num_steps = 1101  # Number of time steps (including initial and final)
initial_time = 3
final_time = 7
initial_value = 47

# Create an array of time points from 43 to 54
time_points = np.linspace(initial_time, final_time, num_steps)

# Create an array to store the Brownian motion trajectories
brownian_trajectories = np.zeros((num_trajectories, num_steps))

# Generate Brownian motion trajectories
for i in range(num_trajectories):
    # Generate normally distributed random increments
    increments = np.random.normal(0, np.sqrt(final_time - initial_time), num_steps - 1)

    # Compute the cumulative sum to simulate Brownian motion
    brownian_path = np.cumsum(increments)+initial_value

    # Set the initial value at time 43
    brownian_path = np.insert(brownian_path, 0, initial_value)

    # Store the trajectory
    brownian_trajectories[i] = brownian_path

# Plot the Brownian motion trajectories
fig, ax = plt.subplots()

for i in range(num_trajectories):
    ax.plot(time_points, brownian_trajectories[i],color='blue',alpha=.1,linewidth=.3)

ax.axvline(x=initial_time, color='black', linestyle='--', label='')
ax.axvline(x=final_time, color='black', linestyle='--', label='')

# Turn off tick labels for both x and y axes
ax.set_xticks([initial_time,final_time],[r'$t$',r'$t+\delta t$'])  # Remove x-axis tick labels
ax.set_yticks([])  # Remove y-axis tick labelsplt.show()
ax.set(xlim = [0,10],
       xlabel = 'Time',
       ylabel = r'$x(t)$')

# Save the plot as a PDF file
fig.savefig("rv_from_sp.pdf", dpi=300, bbox_inches='tight', format='pdf')
plt.close(fig)