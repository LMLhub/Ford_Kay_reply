#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 08:38:30 2023

@author: ole
"""

import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
seed_value = 42
np.random.seed(seed_value)

# Define parameters for the GBM
mu = 0.05  # Drift
sigma = 0.3  # Volatility
S0 = 1  # Initial price
T = 10000.0  # Time period (1 year)
dt = 1.  # Time step (daily data for 1 year)

# Define parameters for the GBM2
mu2 = 0.02  # Drift
sigma2 = 0.1  # Volatility

# Generate time points
t = np.arange(0, T+dt, dt)

# Generate GBM data
W = np.random.randn(len(t))
W = np.cumsum(W) * np.sqrt(dt)  # Brownian motion
X = (mu - 0.5 * sigma**2) * t + sigma * W
S = S0 * np.exp(X)  # Geometric Brownian motion

# Generate GBM data
W2 = np.random.randn(len(t))
W2 = np.cumsum(W) * np.sqrt(dt)  # Brownian motion
X2 = (mu2 - 0.5 * sigma2**2) * t + sigma * W
S2 = S0 * np.exp(X2)  # Geometric Brownian motion

# Create the figure and axes
fig, ax1 = plt.subplots()

# Plot GBM on the left y-axis
ax1.set_xlabel('Time')
ax1.set_ylabel(r'$f(x_A), f(x_B)$', color='tab:red')
ax1.plot(t, np.log(S), color='tab:red', zorder=2)
ax1.plot(t, np.log(S2), color='tab:red', zorder=2)
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a twin y-axis for the logarithm
ax2 = ax1.twinx()
ax2.set_ylabel(r'$x_A, x_B$', color='tab:blue')
ax2.plot(t, S, color='tab:blue', zorder=2)
ax2.plot(t, S2, color='tab:blue', zorder=2)
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Title and labels
plt.xlabel('Time')

# Save the plot as a PDF file
plt.savefig('ergodicity_transform_1.pdf', format='pdf')

# Display the plot
plt.show()


dS=S[:-1]-S[1:]
dS2=S2[:-1]-S2[1:]
# Create the figure and axes
fig, ax3 = plt.subplots()

# Plot GBM on the left y-axis
ax3.set_xlabel('Time')
ax3.set_ylabel(r'$\delta f(x_A), \delta f(x_B)$', color='tab:red')
ax3.plot(t[:-1], np.log(S[:-1])-np.log(S[1:]), color='tab:red',linewidth=.1)
ax3.plot(t[:-1], np.log(S2[:-1])-np.log(S2[1:]), color='tab:red', alpha=1,linewidth=.1)
ax3.tick_params(axis='y', labelcolor='tab:red')

# Create a twin y-axis for the logarithm
ax4 = ax3.twinx()
ax4.set_ylabel(r'$\delta x_A, \delta x_B$', color='tab:blue')
ax4.plot(t[:-1], dS, color='tab:blue')
ax4.plot(t[:-1], dS2, color='tab:blue')
ax4.tick_params(axis='y', labelcolor='tab:blue')

# Title and labels
plt.xlabel('Time')

# Save the plot as a PDF file
plt.savefig('ergodicity_transform_2.pdf', format='pdf')
