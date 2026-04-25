import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

bandwidth = 10e6
rtt = 80e-3
packet_size_bits = 1000 * 8
window_size = 8
lost_packet_number = 4

tx_time = packet_size_bits / bandwidth
stop_wait_util = tx_time / (rtt + tx_time)
required_window = (rtt + tx_time) / tx_time

gbn_retx = window_size - lost_packet_number + 1
sr_retx = 1

print(f"Transmission time: {tx_time*1000:.4f} ms")
print(f"Stop-and-Wait utilization: {stop_wait_util*100:.4f}%")
print(f"Required window for full utilization: {required_window:.2f}")
print(f"GBN retransmissions after packet 4 loss: {gbn_retx}")
print(f"SR retransmissions after packet 4 loss: {sr_retx}")

windows = np.arange(1, 151)
utilizations = np.minimum(1, windows * tx_time / (rtt + tx_time))

plt.figure(figsize=(9, 6))
plt.plot(windows, utilizations * 100)
plt.axvline(required_window, linestyle="--", label=f"Full utilization window ≈ {required_window:.1f}")
plt.xlabel("Window size")
plt.ylabel("Utilization (%)")
plt.title("Sliding Window Utilization")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/sliding_window_utilization.png", dpi=200)
plt.show()

loss_probs = np.linspace(0, 0.2, 100)
window = 8

# Approximate expected retransmissions per window:
# SR retransmits expected number of lost packets.
# GBN retransmits from first lost packet onward. If no loss, zero.
sr_expected = window * loss_probs

gbn_expected = []
for p in loss_probs:
    exp = 0
    for first_loss in range(1, window + 1):
        prob_first_loss = ((1 - p) ** (first_loss - 1)) * p
        exp += prob_first_loss * (window - first_loss + 1)
    gbn_expected.append(exp)

plt.figure(figsize=(9, 6))
plt.plot(loss_probs, sr_expected, label="Selective Repeat")
plt.plot(loss_probs, gbn_expected, label="Go-Back-N")
plt.xlabel("Packet loss probability")
plt.ylabel("Expected retransmissions per window")
plt.title("Expected Retransmissions: GBN vs SR")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/gbn_vs_sr_retransmissions.png", dpi=200)
plt.show()
