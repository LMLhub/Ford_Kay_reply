#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:24:54 2023

@author: Benjamin Skjold
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

# Define parameters for simulations
X0 = 1.0
T = 750
M = 50
g = 21/20
r = 5/20

# Define analytical formulae
def ExpectedxT(X0, t, g, r):
    return X0 * ((g)**t)

def ExpectedgammaT(g, r):
    return 1/2 * (np.log(g + r) + np.log(g - r))

def StdDevxT(X0, t, g, r):
    return X0 * np.sqrt((g**2 + r**2)**t - g**(2*t))

def TypicalxT(X0, t, g, r):
    return X0 * ( np.sqrt(g**2 - r**2))**t

def Tstar(g,r):
    num = np.log(np.sqrt((g+r)/(g-r)))
    den = np.log(np.sqrt(g**2 - r**2))
    return (num/den)**2

def gMeanxT(X0, t, g, r):
    return X0 * np.sqrt(g**2 - r**2)**t

def gStdDevxT(X0, t, g, r):
    return X0 * np.exp((np.sqrt(t)/2) * np.sqrt(np.log(g+r) - np.log(g-r)))

# Generate M trajectories
X = np.zeros((T+1, M))
gamma = np.zeros((T+1, M))
B = np.random.randint(2, size=(T, M))

def f(x, b, g, r):
    return x * (g + r) if b == 0 else x * (g - r)

X[0, :] = X0
gamma[0, :] = 0

for i in range(1, T+1):
    for j in range(M):
        c = B[i-1, j]
        X[i, j] = f(X[i - 1, j], c, g, r)
        gamma[i, j] = np.log(X[i, j]) / i

# Calculate expected, typical, and standard deviation values
expectedValue = np.array([ExpectedxT(X0, t, g, r) for t in range(T+1)])
typicalValue = np.array([TypicalxT(X0, t, g, r) for t in range(T+1)])
stddevValues = np.array([StdDevxT(X0, t, g, r) for t in range(T+1)])

# Calculate geometric mean and standard deviation
gMeanValues = np.array([gMeanxT(X0, t, g, r) for t in range(T+1)])
gstddevValues = np.array([gStdDevxT(X0, t, g, r) for t in range(T+1)])

# Calculate upper and lower bounds for uncertainty interval
spreadUpperValues = gMeanValues * gstddevValues
spreadLowerValues = gMeanValues / gstddevValues

# Create plots
fig, ax = plt.subplots()
ax.set(yscale = 'log',
       xlabel = 'Time',
       ylabel = 'XT')

for i in range(M):
    ax.plot(range(T+1), X[:, i], color='grey', alpha = 0.5)
ax.plot([], color = 'grey', alpha = 0.5, label = '$X_T$ sample trajectories')
ax.plot(range(T+1), expectedValue, label='$X_T$ expectation', color='blue')
ax.plot(range(T+1), typicalValue, label='$X_T$ most likely value', color='green')
ax.plot(range(T+1), spreadUpperValues, label='Uncertainty interval', color='orange')
ax.plot(range(T+1), spreadLowerValues, color='orange')

ax.legend(loc='upper left')
fig.savefig("peters_coin_toss1.pdf", dpi=300, bbox_inches='tight', format='pdf')
plt.close(fig)

# Calculate expected growth rate values
expectedValueGrowthRate = np.array([ExpectedgammaT(g, r) for t in range(T+1)])

# Create plots for growth rate trajectories
fig, ax = plt.subplots()
ax.set(xlabel = 'Time',
       ylabel = '$\gamma_T$')

for i in range(M):
    ax.plot(range(T+1), gamma[:, i], color = 'grey', alpha = 0.5)

ax.plot(range(T+1), expectedValueGrowthRate, label='$\gamma_T$ expectation', color='blue')
ax.plot([], color = 'grey', alpha = 0.5, label = 'Sample $\gamma$ trajectories')

ax.axvline(x=Tstar(g,r), color='gray', linestyle='--', label= '$T^*$')

ax.legend(loc='upper right')
fig.savefig("peters_coin_toss2.pdf", dpi=300, bbox_inches='tight', format='pdf')
