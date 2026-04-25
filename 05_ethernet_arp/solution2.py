import random
import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------
num_hosts = 30
time_steps = 200
ttl = 10  # cache lifetime

hosts = list(range(num_hosts))

# ARP cache: host -> {dest: expiry_time}
arp_cache = {h: {} for h in hosts}

broadcasts_per_time = []

# -----------------------------
# Simulation
# -----------------------------
for t in range(time_steps):
    broadcasts = 0

    # Expire cache
    for h in hosts:
        expired = [d for d, exp in arp_cache[h].items() if exp <= t]
        for d in expired:
            del arp_cache[h][d]

    # Each host tries to send
    for h in hosts:
        dest = random.choice([x for x in hosts if x != h])

        if dest not in arp_cache[h]:
            # ARP broadcast
            broadcasts += 1

            # Update cache
            arp_cache[h][dest] = t + ttl

    broadcasts_per_time.append(broadcasts)

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(broadcasts_per_time)
plt.xlabel("Time")
plt.ylabel("ARP Broadcasts")
plt.title("ARP Broadcast Behavior Over Time")
plt.grid()
plt.show()