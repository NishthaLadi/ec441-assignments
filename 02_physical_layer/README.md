# Topic 2 — Physical Layer: Guided Media and Digital Signaling

**Artifact type:** Problem + code  
**Course topic:** Physical layer: media, propagation, signals, noise, data rates

## Problem

A guided copper channel has:

- Bandwidth: \(2.5\text{ MHz}\)
- Signal levels: \(M = 32\)
- SNR: \(25\text{ dB}\)

Answer the following:

1. Compute the maximum bit rate using the Nyquist formula.
2. Compute Shannon capacity.
3. Which limit is the bottleneck?
4. If the system designer doubles signal levels from 32 to 64, does the practical maximum rate improve?
5. Find the minimum SNR required for a 30 Mbps reliable channel at the same bandwidth.
6. Plot Nyquist rate vs signal levels and Shannon capacity vs SNR.

## Worked Solution

Nyquist limit for a noiseless channel is:

\[
R_N = 2B\log_2(M)
\]

\[
R_N = 2(2.5\times10^6)\log_2(32)
\]

\[
R_N = 5\times10^6 \times 5 = 25\text{ Mbps}
\]

Convert SNR:

\[
SNR = 10^{25/10} = 316.23
\]

Shannon capacity is:

\[
C = B\log_2(1+SNR)
\]

\[
C = 2.5\times 10^6 \log_2(317.23)
\]

\[
C \approx 20.77\text{ Mbps}
\]

The actual usable upper bound is:

\[
\min(R_N, C) = 20.77\text{ Mbps}
\]

So the bottleneck is **noise/Shannon capacity**, not the number of signal levels.

If signal levels increase to \(M=64\):

\[
R_N = 2(2.5\times10^6)\log_2(64)
\]

\[
R_N = 30\text{ Mbps}
\]

But Shannon capacity is still about 20.77 Mbps, so the actual practical maximum rate does not improve unless SNR also improves.

For a target rate of 30 Mbps:

\[
30\times10^6 = 2.5\times10^6\log_2(1+SNR)
\]

\[
12 = \log_2(1+SNR)
\]

\[
1+SNR = 2^{12}
\]

\[
SNR = 4095
\]

\[
SNR_{dB}=10\log_{10}(4095) \approx 36.12\text{ dB}
\]

## Interpretation

Increasing the number of signal levels only helps when the channel is not already limited by noise. With high-order signaling, symbols become closer together and more vulnerable to noise.
