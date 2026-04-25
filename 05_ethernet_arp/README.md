# Topic 5 — Ethernet: Addressing, Switching, and ARP

**Artifact type:** Problem + simulation  
**Course topic:** Ethernet: addressing, switching, ARP

## Problem

A switched Ethernet LAN has 50 hosts. Each host contacts 8 randomly selected destination hosts per minute. If a host does not know the destination MAC address, it sends an ARP request. ARP requests are broadcast; ARP replies are unicast.

Compare two ARP cache TTL values:

- Short TTL: 30 seconds
- Long TTL: 120 seconds

Answer the following:

1. If every destination is initially unknown, how many ARP requests happen in the first minute?
2. How many host-level broadcast receptions are generated in that first minute?
3. How many ARP replies are generated?
4. Simulate ARP behavior for 20 minutes under both TTL values.
5. Explain why increasing TTL reduces overhead but can also risk stale mappings.

## Worked Solution

There are 50 hosts and each contacts 8 unknown destinations initially:

\[
50 \times 8 = 400
\]

So there are 400 ARP requests in the first minute.

Each ARP request is broadcast to all other hosts:

\[
400 \times (50-1) = 19,600
\]

So the LAN experiences 19,600 host-level broadcast receptions.

Each ARP request should produce one ARP reply:

\[
400 \text{ replies}
\]

A longer TTL means entries remain cached longer, so repeated communication with the same destination does not require another broadcast. However, if a machine changes its MAC address or moves, stale ARP cache entries may cause failed delivery until the entry expires.

## Interpretation

ARP is efficient for occasional discovery, but broadcast traffic can become expensive in large LANs. Caching is essential because it turns repeated communication from broadcast-based discovery into unicast forwarding.

## Insights:
- ARP broadcasts spike when cache expires
- Increasing TTL reduces broadcast frequency
- However, large TTL risks stale entries

## Conclusion:
There is a tradeoff between network overhead and accuracy of ARP mappings.
