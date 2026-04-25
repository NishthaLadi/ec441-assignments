import os
import ipaddress
import math
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

base = ipaddress.ip_network("10.20.0.0/16")

departments = {
    "Engineering": 900,
    "Research": 420,
    "Operations": 180,
    "HR": 75,
    "Guest WiFi": 50,
}

def subnet_requirement(hosts):
    host_bits = math.ceil(math.log2(hosts + 2))
    prefix = 32 - host_bits
    total = 2 ** host_bits
    usable = total - 2
    waste = usable - hosts
    return prefix, total, usable, waste

def align_to_prefix(current_ip_int, prefix):
    while True:
        candidate = ipaddress.ip_network((current_ip_int, prefix), strict=False)
        if int(candidate.network_address) == current_ip_int:
            return candidate
        current_ip_int += 1

rows = []
current_ip = int(base.network_address)

for department, hosts in sorted(departments.items(), key=lambda x: x[1], reverse=True):
    prefix, total, usable, waste = subnet_requirement(hosts)
    network = align_to_prefix(current_ip, prefix)
    host_list = list(network.hosts())

    rows.append({
        "Department": department,
        "Required Hosts": hosts,
        "CIDR": str(network),
        "Prefix": f"/{prefix}",
        "Network": str(network.network_address),
        "First Usable": str(host_list[0]),
        "Last Usable": str(host_list[-1]),
        "Broadcast": str(network.broadcast_address),
        "Usable Capacity": usable,
        "Wasted Usable IPs": waste,
    })

    current_ip = int(network.broadcast_address) + 1

df = pd.DataFrame(rows)
print(df.to_string(index=False))
print("\nTotal wasted usable IPs:", df["Wasted Usable IPs"].sum())

df.to_csv("outputs/subnet_allocation.csv", index=False)

plt.figure(figsize=(10, 6))
x = range(len(df))
plt.bar(x, df["Usable Capacity"], label="Usable capacity")
plt.plot(x, df["Required Hosts"], marker="o", label="Required hosts")
plt.xticks(x, df["Department"], rotation=30, ha="right")
plt.ylabel("Number of hosts")
plt.title("VLSM Subnet Allocation Efficiency")
plt.grid(axis="y")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/subnet_allocation_efficiency.png", dpi=200)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df["Department"], df["Wasted Usable IPs"])
plt.ylabel("Wasted usable IPs")
plt.title("Wasted Addresses by Department")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("outputs/subnet_waste.png", dpi=200)
plt.show()
