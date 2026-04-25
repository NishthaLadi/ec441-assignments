# Topic 1 — Information Theory and Networking

**Artifact type:** Problem + code  
**Course topic:** Information: sources and representation

## Problem

A network sensor sends one symbol every microsecond. The source alphabet is:

| Symbol | Probability |
|---|---:|
| A | 0.40 |
| B | 0.30 |
| C | 0.20 |
| D | 0.10 |

The communication channel has:

- Bandwidth: \(B = 4\text{ MHz}\)
- Signal-to-noise ratio: \(18\text{ dB}\)
- Practical coding overhead: 12%

Answer the following:

1. Compute the entropy of the source in bits/symbol.
2. Compute the raw information rate of the source.
3. Compute Shannon capacity of the channel.
4. After adding 12% coding overhead, can this source be transmitted reliably?
5. Determine the maximum symbol rate supported by the channel.
6. Use Python to plot channel capacity for SNR values from 0 to 30 dB and bandwidths of 1 MHz, 2 MHz, and 4 MHz.

## Worked Solution

Entropy is:

\[
H(X) = -\sum_i p_i \log_2(p_i)
\]

\[
H(X) = -(0.4\log_2(0.4)+0.3\log_2(0.3)+0.2\log_2(0.2)+0.1\log_2(0.1))
\]

\[
H(X) \approx 1.846 \text{ bits/symbol}
\]

The source sends one symbol every microsecond:

\[
f_s = 10^6 \text{ symbols/s}
\]

So the raw source information rate is:

\[
R = H(X)f_s = 1.846 \times 10^6
\]

\[
R \approx 1.846 \text{ Mbps}
\]

With 12% coding overhead:

\[
R_{\text{coded}} = 1.12R
\]

\[
R_{\text{coded}} \approx 2.068 \text{ Mbps}
\]

Convert SNR from dB to linear scale:

\[
SNR = 10^{18/10} \approx 63.10
\]

Shannon capacity is:

\[
C = B\log_2(1+SNR)
\]

\[
C = 4 \times 10^6 \log_2(1+63.10)
\]

\[
C \approx 24.01 \text{ Mbps}
\]

Since:

\[
2.068 \text{ Mbps} < 24.01 \text{ Mbps}
\]

the source can be transmitted reliably in theory.

The maximum symbol rate supported, assuming the same entropy and overhead, is:

\[
f_{s,\max} = \frac{C}{1.12H(X)}
\]

\[
f_{s,\max} \approx \frac{24.01\times 10^6}{1.12 \times 1.846}
\]

\[
f_{s,\max} \approx 11.61 \times 10^6 \text{ symbols/s}
\]

## Interpretation

The important insight is that SNR gives logarithmic improvement, while bandwidth gives linear improvement. After a certain SNR, increasing bandwidth is usually more effective than trying to improve SNR by a small amount.
