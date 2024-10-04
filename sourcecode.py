import numpy as np
import matplotlib.pyplot as plt

# Number of random points to generate
num_points = 100

# Generate random x-coordinates between 0 and 2*pi
x = np.random.uniform(0, 2 * np.pi, num_points)

# Compute corresponding y-coordinates using the sine function
y = np.sin(x)

# Generate random offsets for the y-coordinates
offsets = np.random.uniform(-0.5, 0.5, num_points)

# Add offsets to the y-coordinates
y += offsets

# Plot the points
plt.scatter(x, y, color='blue', s=10)

# Plot the sine curve
x_vals = np.linspace(0, 2 * np.pi, 100)
y_vals = np.sin(x_vals)
plt.plot(x_vals, y_vals, color='red')