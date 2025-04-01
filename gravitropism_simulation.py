import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
steps = 20  # number of growth steps
stem_x = [0]  # start of the plant stem (X axis)
stem_y = [0]  # start of the plant stem (Y axis)

# Simulated "gravitropism" behavior
for i in range(steps):
    # Auxin causes uneven growth: slight random "correction" against gravity
    angle = np.radians(90 + np.random.uniform(-20, 20))  # 90° = straight up
    dx = np.cos(angle)
    dy = np.sin(angle)

    # New point of the stem
    new_x = stem_x[-1] + dx
    new_y = stem_y[-1] + dy

    stem_x.append(new_x)
    stem_y.append(new_y)

# Plotting
plt.figure(figsize=(6, 10))
plt.plot(stem_x, stem_y, marker='o', color='green')
plt.title("Simulated Plant Stem Growth Against Gravity")
plt.xlabel("Horizontal Position")
plt.ylabel("Vertical Position")
plt.grid(True)
plt.axis("equal")
plt.show()
