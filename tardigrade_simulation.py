import matplotlib.pyplot as plt
import numpy as np

# Define gravity range (in Gs)
g_force = np.linspace(1, 10000, 500)

# Simulated "stress response" functions
def stress_normal(g):
    return g ** 1.2  # stress increases steeply

def stress_cryptobiosis(g):
    return g ** 0.6  # flatter curve = more resistance

# Calculate stress for each G
stress_no_protection = stress_normal(g_force)
stress_with_protection = stress_cryptobiosis(g_force)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(g_force, stress_no_protection, label="Normal State", linestyle="--")
plt.plot(g_force, stress_with_protection, label="Cryptobiosis", linewidth=2)
plt.xlabel("Gravity (in Gs)")
plt.ylabel("Estimated Biological Stress")
plt.title("Tardigrade Stress Response to Increasing Gravity")
plt.legend()
plt.grid(True)
plt.show()
