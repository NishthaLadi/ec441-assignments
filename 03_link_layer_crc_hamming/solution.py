import os
import itertools
import random
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

def mod2_division(bitstring, generator):
    data = list(bitstring)
    gen = list(generator)

    for i in range(len(data) - len(gen) + 1):
        if data[i] == "1":
            for j in range(len(gen)):
                data[i + j] = "0" if data[i + j] == gen[j] else "1"

    return "".join(data[-(len(generator)-1):])

def crc_encode(dataword, generator):
    zeros = "0" * (len(generator) - 1)
    remainder = mod2_division(dataword + zeros, generator)
    return dataword + remainder, remainder

def crc_check(frame, generator):
    return mod2_division(frame, generator) == "0" * (len(generator)-1)

def flip_positions(bitstring, positions):
    bits = list(bitstring)
    for pos in positions:
        bits[pos] = "1" if bits[pos] == "0" else "0"
    return "".join(bits)

dataword = "1011101"
generator = "1101"

frame, remainder = crc_encode(dataword, generator)

print(f"Dataword: {dataword}")
print(f"Generator: {generator}")
print(f"CRC remainder: {remainder}")
print(f"Transmitted frame: {frame}")
print(f"Uncorrupted frame accepted? {crc_check(frame, generator)}")

single_error = flip_positions(frame, [2])
print(f"Single-bit corrupted frame: {single_error}")
print(f"Single-bit error detected? {not crc_check(single_error, generator)}")

# Exhaustive detection for k-bit errors
detection_rates = {}
n = len(frame)

for k in [1, 2, 3]:
    total = 0
    detected = 0

    for positions in itertools.combinations(range(n), k):
        corrupted = flip_positions(frame, positions)
        total += 1
        if not crc_check(corrupted, generator):
            detected += 1

    detection_rates[k] = detected / total
    print(f"{k}-bit error detection rate: {detection_rates[k]*100:.2f}%")

plt.figure(figsize=(8, 5))
plt.bar([str(k) for k in detection_rates.keys()], [v * 100 for v in detection_rates.values()])
plt.xlabel("Number of flipped bits")
plt.ylabel("Detection rate (%)")
plt.title("CRC Detection Rate by Error Weight")
plt.ylim(0, 105)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("outputs/crc_detection_rates.png", dpi=200)
plt.show()

def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

# Generate 4-bit even parity codewords: 3 data bits + 1 parity bit
codewords = []
for bits in itertools.product("01", repeat=3):
    data = "".join(bits)
    parity_bit = "0" if data.count("1") % 2 == 0 else "1"
    codewords.append(data + parity_bit)

distances = [
    hamming_distance(a, b)
    for a, b in itertools.combinations(codewords, 2)
]

print("Even parity codewords:", codewords)
print("Minimum Hamming distance:", min(distances))

plt.figure(figsize=(8, 5))
plt.hist(distances, bins=np.arange(1, 6) - 0.5, edgecolor="black")
plt.xticks(range(1, 6))
plt.xlabel("Pairwise Hamming distance")
plt.ylabel("Frequency")
plt.title("Hamming Distance Distribution for Even-Parity Codewords")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("outputs/hamming_distance_distribution.png", dpi=200)
plt.show()
