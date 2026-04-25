import random
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation Parameters
# -----------------------------
num_nodes = 50
time_slots = 1000
transmission_prob = 0.05  # probability a node transmits in a slot

successful = 0
collisions = 0
idle = 0

throughput = []

# -----------------------------
# Simulation Loop
# -----------------------------
for t in range(time_slots):
    transmitting_nodes = []

    for node in range(num_nodes):
        if random.random() < transmission_prob:
            transmitting_nodes.append(node)

    if len(transmitting_nodes) == 0:
        idle += 1
    elif len(transmitting_nodes) == 1:
        successful += 1
    else:
        collisions += 1

    throughput.append(successful / (t + 1))

# -----------------------------
# Results
# -----------------------------
print("Total Slots:", time_slots)
print("Successful transmissions:", successful)
print("Collisions:", collisions)
print("Idle slots:", idle)

# -----------------------------
# Plot Throughput Over Time
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(throughput)
plt.xlabel("Time Slot")
plt.ylabel("Throughput")
plt.title("ALOHA Throughput Simulation")
plt.grid()
plt.show()