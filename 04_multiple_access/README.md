# Topic 4 — Multiple Access: ALOHA and CSMA

**Artifact type:** Problem + simulation  
**Course topic:** Multiple access: ALOHA, CSMA

## Problem

A shared broadcast channel has \(N=40\) stations. During each time slot, each station independently attempts transmission with probability \(p\).

Answer the following:

1. Derive the probability that a slot contains exactly one successful transmission.
2. Find the value of \(p\) that maximizes successful slots.
3. Compute maximum success probability for \(N=40\).
4. Compare this discrete slotted model to the theoretical Slotted ALOHA throughput:

\[
S = Ge^{-G}
\]

5. Simulate 10,000 slots for different values of \(p\).
6. Explain what happens when \(p\) is too small or too large.

## Worked Solution

A slot is successful if exactly one station transmits. This follows a binomial distribution:

\[
P(\text{success}) = \binom{N}{1}p(1-p)^{N-1}
\]

\[
P(\text{success}) = Np(1-p)^{N-1}
\]

The maximum occurs at approximately:

\[
p = \frac{1}{N}
\]

For \(N=40\):

\[
p = \frac{1}{40} = 0.025
\]

\[
P_{\max} = 40(0.025)(0.975)^{39}
\]

\[
P_{\max} \approx 0.372
\]

This is close to:

\[
\frac{1}{e} \approx 0.368
\]

which matches the ideal Slotted ALOHA maximum.

## Interpretation

If \(p\) is too small, most slots are idle. If \(p\) is too large, many stations transmit at once, causing collisions. The best operating point balances idle time and collision probability.

## Insights:
- At low transmission probability → mostly idle
- At high probability → collisions dominate
- Optimal throughput occurs at balanced load

## Conclusion:
Real systems must regulate transmission probability (CSMA does this better than ALOHA).
