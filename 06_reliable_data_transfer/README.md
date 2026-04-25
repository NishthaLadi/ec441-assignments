# Topic 6 — Reliable Data Transfer: Stop-and-Wait, GBN, and SR

**Artifact type:** Problem + simulation  
**Course topic:** Reliable data transfer: Stop-and-Wait, sliding window, Go-Back-N, Selective Repeat

## Problem

A reliable transport protocol sends packets over a link with:

- Bandwidth: \(10\text{ Mbps}\)
- RTT: \(80\text{ ms}\)
- Packet size: \(1000\text{ bytes}\)
- Window size: 8 packets
- Packet 4 in the window is lost

Answer the following:

1. Compute packet transmission time.
2. Compute Stop-and-Wait utilization.
3. Compute the minimum window size needed to fully utilize the link.
4. If packet 4 is lost, how many packets are retransmitted under Go-Back-N?
5. How many packets are retransmitted under Selective Repeat?
6. Simulate throughput as window size varies from 1 to 150.
7. Simulate expected retransmissions for GBN and SR as packet loss probability varies.

## Worked Solution
(same solution in the code)
Packet size:

\[
1000\text{ bytes} = 8000\text{ bits}
\]

Transmission time:

\[
T_t = \frac{8000}{10\times10^6}
\]

\[
T_t = 0.0008\text{ s} = 0.8\text{ ms}
\]

Stop-and-Wait utilization:

\[
U = \frac{T_t}{RTT + T_t}
\]

\[
U = \frac{0.8}{80 + 0.8}
\]

\[
U \approx 0.0099 = 0.99\%
\]

Minimum window size for full utilization:

\[
W \ge \frac{RTT + T_t}{T_t}
\]

\[
W \ge \frac{80.8}{0.8} = 101
\]

If packet 4 is lost in a window of 8:

- Go-Back-N retransmits packets 4, 5, 6, 7, and 8 = 5 packets.
- Selective Repeat retransmits only packet 4 = 1 packet.

## Interpretation

Stop-and-Wait wastes most link capacity on high-delay links. Sliding windows solve this by allowing multiple packets in flight. Selective Repeat is more efficient during loss, but it requires more receiver buffering and more complex acknowledgments.
