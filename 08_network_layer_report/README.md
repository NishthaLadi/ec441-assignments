# Topic 8 — Network Layer Report: CIDR, Subnetting, and VLSM

**Artifact type:** Report + code  
**Course topic:** Network layer: forwarding, routing, IP addressing, CIDR, subnetting

## Report Question

A company receives the block:

```text
10.20.0.0/16
```

It must allocate subnets for five departments:

| Department | Required Hosts |
|---|---:|
| Engineering | 900 |
| Research | 420 |
| Operations | 180 |
| HR | 75 |
| Guest WiFi | 50 |

The company wants to minimize wasted addresses while keeping the routing table simple.

## Tasks

1. Use VLSM to allocate subnet blocks.
2. For each subnet, compute:
   - CIDR block
   - network address
   - first usable address
   - last usable address
   - broadcast address
   - usable host capacity
   - wasted usable IPs
3. Compute total address waste.
4. Explain why subnets should be allocated from largest to smallest.
5. Discuss the tradeoff between efficient address use and route aggregation.

## Worked Report
(check subnetting_report.md)
### Method

For each department, choose the smallest subnet where:

\[
2^h - 2 \ge \text{required hosts}
\]

where \(h\) is the number of host bits.

The prefix length is:

\[
/(32-h)
\]

Departments should be allocated largest to smallest to avoid fragmentation. If smaller subnets are placed first, it may become harder to place a large contiguous subnet later.

### Engineering

Engineering needs 900 hosts.

\[
2^{10}-2 = 1022
\]

So Engineering needs 10 host bits:

\[
/22
\]

### Research

Research needs 420 hosts.

\[
2^9 - 2 = 510
\]

So Research needs:

\[
/23
\]

### Operations

Operations needs 180 hosts.

\[
2^8 - 2 = 254
\]

So Operations needs:

\[
/24
\]

### HR

HR needs 75 hosts.

\[
2^7 - 2 = 126
\]

So HR needs:

\[
/25
\]

### Guest WiFi

Guest WiFi needs 50 hosts.

\[
2^6 - 2 = 62
\]

So Guest WiFi needs:

\[
/26
\]

### Address Waste

Waste is calculated as:

\[
\text{waste} = \text{usable addresses} - \text{required hosts}
\]

### Routing Table Discussion

VLSM minimizes waste, but many small subnets can increase forwarding table size. If subnets are allocated contiguously, the organization may still summarize them into a larger route, such as `10.20.0.0/16`, when advertising externally. Internally, routers still need more specific entries for each department.

## Interpretation

CIDR and VLSM show the main network-layer design tradeoff: address efficiency versus operational simplicity. The best design minimizes waste while preserving clear boundaries and route summarization opportunities.
