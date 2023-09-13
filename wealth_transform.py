#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 08:38:30 2023

@author: ole
"""

import numpy as np
import matplotlib.pyplot as plt

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
ax1.set_ylabel(r'$x_A, x_B$', color='tab:blue')
ax1.plot(t, S, color='tab:blue')
ax1.plot(t, S2, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a twin y-axis for the logarithm
ax2 = ax1.twinx()
ax2.set_ylabel(r'$f(x_A), f(x_B)$', color='tab:red')
ax2.plot(t, np.log(S), color='tab:red')
ax2.plot(t, np.log(S2), color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Title and labels
plt.xlabel('Time')

# Display the plot
plt.show()