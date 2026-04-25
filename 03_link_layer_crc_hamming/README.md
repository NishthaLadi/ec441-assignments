# Topic 3 — Link Layer: Error Control, CRC, and Hamming Distance

**Artifact type:** Problem + code  
**Course topic:** Link layer: frames, error control, CRC

## Problem

A link-layer protocol sends the dataword:

```text
1011101
```

using the CRC generator polynomial represented by:

```text
1101
```

Answer the following:

1. Compute the CRC remainder.
2. Write the final transmitted frame.
3. Verify that the receiver accepts the uncorrupted frame.
4. Flip one bit and verify whether CRC detects the error.
5. Run a simulation for all possible 1-bit, 2-bit, and 3-bit errors and estimate what fraction are detected.
6. Generate all 4-bit even-parity codewords and compute their minimum Hamming distance.
7. Explain whether even parity can correct any errors.

## Worked Solution

The generator `1101` has length 4, so the CRC remainder has:

\[
r = 4 - 1 = 3
\]

bits.

The sender appends three zeros to the original dataword:

```text
1011101000
```

Then binary polynomial division is performed using XOR instead of subtraction. The remainder is appended to the dataword to form the transmitted frame.

CRC detects an error if the received frame divided by the generator gives a nonzero remainder.

For even parity, the minimum Hamming distance is 2 because any valid codeword differs from another valid codeword in at least two positions. This means even parity can detect all single-bit errors but cannot correct them because \(d_{min}=2\), while correction of one-bit errors requires:

\[
d_{min} \ge 2t+1 = 3
\]

## Interpretation

CRC is stronger than a simple parity bit because it can detect burst errors and many multi-bit errors. However, no CRC generator detects all possible multi-bit errors, so simulation is useful for understanding practical detection strength.
