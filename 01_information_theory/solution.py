import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

probabilities = np.array([0.40, 0.30, 0.20, 0.10])
symbol_rate = 1e6
bandwidth = 4e6
snr_db = 18
coding_overhead = 0.12

entropy = -np.sum(probabilities * np.log2(probabilities))
raw_rate = entropy * symbol_rate
coded_rate = raw_rate * (1 + coding_overhead)

snr_linear = 10 ** (snr_db / 10)
capacity = bandwidth * np.log2(1 + snr_linear)

max_symbol_rate = capacity / ((1 + coding_overhead) * entropy)

print(f"Entropy: {entropy:.4f} bits/symbol")
print(f"Raw source rate: {raw_rate / 1e6:.4f} Mbps")
print(f"Coded source rate: {coded_rate / 1e6:.4f} Mbps")
print(f"Channel capacity: {capacity / 1e6:.4f} Mbps")
print(f"Can transmit reliably? {coded_rate <= capacity}")
print(f"Maximum supported symbol rate: {max_symbol_rate / 1e6:.4f} Msymbols/s")

snr_db_values = np.linspace(0, 30, 200)
bandwidth_values = [1e6, 2e6, 4e6]

plt.figure(figsize=(9, 6))
for B in bandwidth_values:
    snr_values = 10 ** (snr_db_values / 10)
    capacities = B * np.log2(1 + snr_values)
    plt.plot(snr_db_values, capacities / 1e6, label=f"B = {B/1e6:.0f} MHz")

plt.axhline(coded_rate / 1e6, linestyle="--", label="Coded source rate")
plt.xlabel("SNR (dB)")
plt.ylabel("Capacity (Mbps)")
plt.title("Shannon Capacity vs SNR")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/information_capacity_vs_snr.png", dpi=200)
plt.show()
