import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

B = 2.5e6
M = 32
snr_db = 25

nyquist = 2 * B * np.log2(M)
snr_linear = 10 ** (snr_db / 10)
shannon = B * np.log2(1 + snr_linear)
actual = min(nyquist, shannon)

target_rate = 30e6
required_snr_linear = 2 ** (target_rate / B) - 1
required_snr_db = 10 * np.log10(required_snr_linear)

print(f"Nyquist rate: {nyquist / 1e6:.4f} Mbps")
print(f"Shannon capacity: {shannon / 1e6:.4f} Mbps")
print(f"Actual upper bound: {actual / 1e6:.4f} Mbps")
print(f"Required SNR for 30 Mbps: {required_snr_db:.4f} dB")

M_values = np.array([2, 4, 8, 16, 32, 64, 128, 256])
nyquist_rates = 2 * B * np.log2(M_values)

plt.figure(figsize=(9, 6))
plt.plot(M_values, nyquist_rates / 1e6, marker="o")
plt.axhline(shannon / 1e6, linestyle="--", label="Shannon capacity at 25 dB")
plt.xscale("log", base=2)
plt.xlabel("Number of signal levels")
plt.ylabel("Nyquist rate (Mbps)")
plt.title("Nyquist Rate vs Signal Levels")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/nyquist_vs_signal_levels.png", dpi=200)
plt.show()

snr_db_values = np.linspace(0, 45, 300)
snr_values = 10 ** (snr_db_values / 10)
capacity_values = B * np.log2(1 + snr_values)

plt.figure(figsize=(9, 6))
plt.plot(snr_db_values, capacity_values / 1e6)
plt.axhline(target_rate / 1e6, linestyle="--", label="30 Mbps target")
plt.axvline(required_snr_db, linestyle="--", label=f"Required SNR = {required_snr_db:.1f} dB")
plt.xlabel("SNR (dB)")
plt.ylabel("Shannon capacity (Mbps)")
plt.title("Shannon Capacity vs SNR")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/shannon_capacity_physical_layer.png", dpi=200)
plt.show()
