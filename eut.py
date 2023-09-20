#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:04:23 2023
@author: ole
"""

import matplotlib.pyplot as plt
import numpy as np
from fig_style_config import figure_size, font_size, label_font_size, legend_font_size, line_width
from scipy.stats import lognorm, norm

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

# Parameters for the normal distributions (of utility)
mu1 = np.mean([np.log(1.5), np.log(.6)])
sigma1 = np.std([np.log(.6), np.log(1.5)])
mu2 = .1
sigma2 = .6

# Implied parameters for the log-normal distributions of wealth
s1 = sigma1
scale1 = np.exp(mu1)
s2 = sigma2
scale2 = np.exp(mu2)

# Generate data points for the x-axis
x = np.linspace(0.0, 2.5, 1000)

# Calculate the probability density function (PDF) for the log-normal distribution
pdflog1 = lognorm.pdf(x, s=s1, scale=scale1)
pdflog2 = lognorm.pdf(x, s=s2, scale=scale2)

# Calculate the probability density function (PDF) for the standard normal distribution
x2 = np.linspace(-1.5, 2.5, 1000)
pdfnorm1 = norm.pdf(x2, loc=mu1, scale=sigma1)
pdfnorm2 = norm.pdf(x2, loc=mu2, scale=sigma2)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, pdflog1, color='blue', linestyle='--', label='Density of $y_A$')
ax.plot(x, pdflog2, color='blue', linestyle='-', label='Density of $y_B$')

ax.plot(x2, pdfnorm1, color='tab:red', linestyle='--', label='Density of $u(y_A)$')
ax.plot(x2, pdfnorm2, color='tab:red', linestyle='-', label='Density of $u(y_B)$')
ax.axvline(x=mu1, color='red', linestyle='--')
ax.axvline(x=mu2, color='red', linestyle='-',)
ax.legend(loc='upper right')
ax.set(xlabel='x, u(x)',
       ylabel='Probability Density',
       xlim=[-1.5, 2.5],
       ylim=[0, 1.1])

# Save the plot as a PDF file
fig.savefig("eut.pdf", dpi=300, bbox_inches='tight', format='pdf')
plt.close(fig)
