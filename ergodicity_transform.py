#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 08:38:30 2023

@author: ole
"""

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
G = (mu - 0.5 * sigma**2)
X = G * t + sigma * W
S = S0 * np.exp(X)  # Geometric Brownian motion

# Generate GBM data
W2 = np.random.randn(len(t))
W2 = np.cumsum(W) * np.sqrt(dt)  # Brownian motion
G2 = (mu2 - 0.5 * sigma2**2)
X2 = G2 * t + sigma * W
S2 = S0 * np.exp(X2)  # Geometric Brownian motion

lightblue = (173/255, 216/255, 230/255)  # (R, G, B)

# Left plot
fig, ax1 = plt.subplots()

# Plot GBM on the left y-axis
ax1.plot(t, np.log(S), color='tab:red', linestyle='-', zorder=0, label=r'$f(x_A(t))$')
ax1.plot(t, np.log(S2), color='tab:pink', linestyle='-', zorder=0, label=r'$f(x_B(t))$')
ax1.plot(t, G * t, color='tab:red', zorder=1)  # Growth rate 1
ax1.plot(t, G2 * t, linestyle='-', color='tab:pink', zorder=1)  # Growth rate 2
ax1.set_ylabel(r'$f$', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a twin y-axis for the logarithm
ax2 = ax1.twinx()
ax2.set_ylabel(r'$x$', color='tab:blue')
ax2.plot(t, S, color='blue', zorder=-1, label=r'$x_A(t)$')
ax2.plot(t, S2, color=lightblue, zorder=-1, label=r'$x_B(t)$')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Title and legend
ax1.set_xlabel('Time')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', ncol=2)

# Save the plot as a PDF file
fig.savefig("ergodicity_transform_1.pdf", dpi=300, bbox_inches='tight', format='pdf')
plt.close(fig)

# Right plot
fig, ax3 = plt.subplots()

# Plot GBM on the left y-axis
ax3.plot(t[:-1], np.log(S[:-1]) - np.log(S[1:]), color='tab:red')
ax3.plot(t[:-1], np.log(S2[:-1]) - np.log(S2[1:]), color='tab:pink')
ax3.set_ylabel(r'$\delta f(x)$', color='tab:red')
ax3.tick_params(axis='y', labelcolor='tab:red')

# Create a twin y-axis for the logarithm
ax4 = ax3.twinx()
ax4.plot(t[:-1], S[:-1] - S[1:], color='blue')
ax4.plot(t[:-1], S2[:-1] - S2[1:], color=lightblue)
ax4.set_ylabel(r'$\delta x$', color='tab:blue')
ax4.tick_params(axis='y', labelcolor='tab:blue')

# Title and labels
ax3.set_xlabel('Time')
ax4.set_xlim([0, 500])
ax4.set_ylim([0, 10000])

# Save the plot as a PDF file
fig.savefig("ergodicity_transform_2.pdf", dpi=300, bbox_inches='tight', format='pdf')
plt.close(fig)