import os
import math
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

devices = 2000
connections_per_device = 70
ports_per_public_ip = 64000
public_ips = 2

required_connections = devices * connections_per_device
capacity = public_ips * ports_per_public_ip
required_ips = math.ceil(required_connections / ports_per_public_ip)

print(f"Required simultaneous connections: {required_connections}")
print(f"Capacity with {public_ips} public IPs: {capacity}")
print(f"Enough capacity? {capacity >= required_connections}")
print(f"Minimum public IPv4 addresses required: {required_ips}")

ip_counts = np.arange(1, 8)
capacities = ip_counts * ports_per_public_ip

plt.figure(figsize=(9, 6))
plt.plot(ip_counts, capacities, marker="o")
plt.axhline(required_connections, linestyle="--", label="Required connections")
plt.xlabel("Number of public IPv4 addresses")
plt.ylabel("NAT connection capacity")
plt.title("NAT Capacity vs Public IPv4 Addresses")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/nat_capacity_vs_public_ips.png", dpi=200)
plt.show()

# Simple dynamic connection occupancy simulation
rng = np.random.default_rng(42)
minutes = 10
seconds = minutes * 60
avg_lifetime = 90

# Assume arrivals are centered around required steady-state occupancy.
# Little's Law: L = lambda * W, so lambda = L / W.
arrival_rate_per_second = required_connections / avg_lifetime

active_expiry_times = []
occupancy = []

for t in range(seconds):
    # Remove expired connections
    active_expiry_times = [expiry for expiry in active_expiry_times if expiry > t]

    # New arrivals
    arrivals = rng.poisson(arrival_rate_per_second)
    lifetimes = rng.exponential(avg_lifetime, size=arrivals)
    active_expiry_times.extend(t + lifetimes)

    occupancy.append(len(active_expiry_times))

plt.figure(figsize=(10, 6))
plt.plot(occupancy)
plt.axhline(capacity, linestyle="--", label=f"Capacity with {public_ips} IPs")
plt.axhline(required_ips * ports_per_public_ip, linestyle="--", label=f"Capacity with {required_ips} IPs")
plt.xlabel("Time (seconds)")
plt.ylabel("Active NAT mappings")
plt.title("Simulated NAT Port Occupancy")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/nat_dynamic_occupancy.png", dpi=200)
plt.show()

peak = max(occupancy)
print(f"Peak simulated NAT mappings: {peak}")
print(f"Public IPs needed for simulated peak: {math.ceil(peak / ports_per_public_ip)}")
