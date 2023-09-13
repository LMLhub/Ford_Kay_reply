#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:04:23 2023

@author: ole
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import lognorm

# Parameters for the normal distributions (of utility)
mu1 = np.mean([np.log(1.5),np.log(.6)])  # Mean
sigma1 = np.std([np.log(.6),np.log(1.5)])  # Standard deviation
mu2 = .1  # Mean
sigma2 = .6  # Standard deviation

# Implied parameters for the log-normal distributions of wealth
s1 = sigma1 #np.sqrt(np.log(1 + (sigma1**2 / mu1**2)))  # Shape parameter
scale1 = np.exp(mu1)  # Scale parameter, set to exp(mean_log(x))
s2 = sigma2 #np.sqrt(np.log(1 + (sigma2**2 / mu2**2)))  # Shape parameter
scale2 = np.exp(mu2)  # Scale parameter, set to exp(mean_log(x))

# Generate data points for the x-axis
x = np.linspace(0.0, 2.5, 1000)  # Start from a small value to avoid log(0)

# Calculate the probability density function (PDF) for the log-normal distribution
pdflog1 = lognorm.pdf(x, s=s1, scale=scale1)
pdflog2 = lognorm.pdf(x, s=s2, scale=scale2)

# Calculate the probability density function (PDF) for the standard normal distribution
x2 = np.linspace(-1.5, 2.5, 1000)
pdfnorm1 = norm.pdf(x2, loc=mu1, scale=sigma1)
pdfnorm2 = norm.pdf(x2, loc=mu2, scale=sigma2)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, pdflog1, color='blue', linestyle='--', label='density of $y_A$')
plt.plot(x, pdflog2, color='blue', linestyle='-',label='density of $y_B$')

plt.plot(x2, pdfnorm1, color='tab:red', linestyle='--', label='density of $u(y_A)$')
plt.axvline(x=mu1, color='red', linestyle='--', label='')
plt.axvline(x=mu2, color='red', linestyle='-', label='')
plt.plot(x2, pdfnorm2, color='tab:red', linestyle='-', label='density of $u(y_B)$')
plt.legend()
plt.xlabel('x, u(x)')
plt.ylabel('probability density')

# Save the plot as a PDF file
plt.savefig('eut.pdf', format='pdf')
plt.show()
