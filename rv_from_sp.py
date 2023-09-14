import matplotlib.pyplot as plt
import numpy as np

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
#plt.figure(figsize=(10, 6))
for i in range(num_trajectories):
    plt.plot(time_points, brownian_trajectories[i],color='blue',alpha=.1,linewidth=.3)

plt.axvline(x=initial_time, color='black', linestyle='--', label='')
plt.axvline(x=final_time, color='black', linestyle='--', label='')

# Turn off tick labels for both x and y axes
ax.set_xticks([initial_time,final_time],[r'$t$',r'$t+\delta t$'])  # Remove x-axis tick labels
ax.set_yticks([])  # Remove y-axis tick labelsplt.show()
plt.xlim([0,10])

plt.xlabel('Time')
plt.ylabel(r'$x(t)$')

# Save the plot as a PDF file
plt.savefig('rv_from_sp.pdf', format='pdf')