import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- 1. Generate Diagrams ---
print("Generating Diagrams...")

# Diagram 1: Capacitor
fig, ax = plt.subplots(figsize=(8, 4))
ax.add_patch(patches.Rectangle((1, 1), 0.2, 4, color='royalblue', ec='black'))
ax.add_patch(patches.Rectangle((6, 1), 0.2, 4, color='crimson', ec='black'))
ax.add_patch(patches.Rectangle((2.5, 1), 2, 4, color='lightgray', alpha=0.8, hatch='///', ec='black'))
ax.text(0.5, 4.5, '+Q', fontsize=12, color='royalblue', fontweight='bold')
ax.text(6.5, 4.5, '-Q', fontsize=12, color='crimson', fontweight='bold')
ax.text(3.5, 2.5, 'Dielectric (K)', ha='center', fontsize=10, bbox=dict(facecolor='white'))
ax.axis('off')
plt.xlim(0, 8)
plt.ylim(0, 6)
plt.savefig('ppc_diagram.png', dpi=300, bbox_inches='tight')
plt.close()

# Diagram 2: RC Circuit
t = np.linspace(0, 5, 200)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(t, 1 - np.exp(-t), 'b', lw=2)
axs[0].set_title('Charging')
axs[1].plot(t, np.exp(-t), 'r', lw=2)
axs[1].set_title('Discharging')
plt.tight_layout()
plt.savefig('rc_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# --- 2. Create Markdown Content ---
markdown_content = r"""
---
title: "Capacitors: Masterclass Notes"
author: "Generated via GitHub Actions"
geometry: margin=1in
header-includes:
 - \usepackage{amsmath}
---

# 1. Capacitance & Dielectrics
$$C = \frac{Q}{V}$$
For Parallel Plate Capacitor:
$$C = \frac{\epsilon_0 A}{d}$$

### Effect of Dielectric
![Dielectric Diagram](ppc_diagram.png)

When a dielectric slab ($K$) is inserted:
*   **Capacitance:** Increases ($KC_0$)
*   **Field:** Decreases ($E_0/K$)

# 2. RC Circuits
Time constant $\tau = RC$.

![RC Graphs](rc_graph.png)

### Charging Equation
$$q(t) = Q_{max}(1 - e^{-t/\tau})$$

### Discharging Equation
$$q(t) = q_0 e^{-t/\tau}$$

# 3. Exam Cheat Sheet (Battery Connected vs Disconnected)

| Quantity | Battery Removed | Battery Connected |
| :--- | :--- | :--- |
| **C** | Increases ($K$) | Increases ($K$) |
| **V** | Decreases ($1/K$) | Constant |
| **U** | Decreases ($1/K$) | Increases ($K$) |
"""

with open('notes.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print("Markdown file created successfully!")
