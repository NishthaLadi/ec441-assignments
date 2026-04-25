import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

N = 40
slots = 10000
p_values = np.linspace(0.001, 0.2, 100)

theoretical_success = N * p_values * (1 - p_values) ** (N - 1)

best_index = np.argmax(theoretical_success)
best_p = p_values[best_index]
best_success = theoretical_success[best_index]

print(f"Best p from sweep: {best_p:.4f}")
print(f"Max theoretical success probability: {best_success:.4f}")
print(f"1/N = {1/N:.4f}")
print(f"1/e = {1/np.e:.4f}")

simulated_success = []
simulated_idle = []
simulated_collision = []

rng = np.random.default_rng(42)

for p in p_values:
    transmissions = rng.binomial(N, p, size=slots)
    simulated_success.append(np.mean(transmissions == 1))
    simulated_idle.append(np.mean(transmissions == 0))
    simulated_collision.append(np.mean(transmissions >= 2))

plt.figure(figsize=(9, 6))
plt.plot(p_values, theoretical_success, label="Theoretical success")
plt.plot(p_values, simulated_success, linestyle="--", label="Simulated success")
plt.plot(p_values, simulated_idle, label="Simulated idle")
plt.plot(p_values, simulated_collision, label="Simulated collision")
plt.axvline(1/N, linestyle="--", label="p = 1/N")
plt.xlabel("Transmit probability p")
plt.ylabel("Slot fraction")
plt.title("Slotted Multiple Access Behavior")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/slotted_multiple_access_simulation.png", dpi=200)
plt.show()

G = np.linspace(0, 5, 300)
pure_aloha = G * np.exp(-2 * G)
slotted_aloha = G * np.exp(-G)

plt.figure(figsize=(9, 6))
plt.plot(G, pure_aloha, label="Pure ALOHA: G exp(-2G)")
plt.plot(G, slotted_aloha, label="Slotted ALOHA: G exp(-G)")
plt.xlabel("Offered load G")
plt.ylabel("Throughput S")
plt.title("Pure ALOHA vs Slotted ALOHA")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/aloha_throughput_comparison.png", dpi=200)
plt.show()
