# Topic 9 — IPv4, IPv6, DHCP, and NAT

**Artifact type:** Problem + simulation  
**Course topic:** IPv4, IPv6, DHCP, NAT

## Problem

A company has:

- 2,000 internal devices
- Each device opens 70 simultaneous TCP connections on average
- The NAT router has 2 public IPv4 addresses
- Each public IPv4 address can safely use 64,000 source ports for NAT/PAT
- During peak hours, connections last an average of 90 seconds

Answer the following:

1. Compute total simultaneous connections required.
2. Compute NAT capacity with 2 public IPv4 addresses.
3. Determine whether 2 public IPs are enough.
4. Compute the minimum number of public IPv4 addresses required.
5. Simulate NAT port occupancy over 10 minutes with random connection arrivals and expirations.
6. Explain how IPv6 changes this design problem.

## Worked Solution

Total simultaneous connections required:

\[
2000 \times 70 = 140,000
\]

Capacity with 2 public IPv4 addresses:

\[
2 \times 64,000 = 128,000
\]

Since:

\[
140,000 > 128,000
\]

two public IPv4 addresses are not enough.

Minimum number of public IPv4 addresses:

\[
\left\lceil \frac{140,000}{64,000} \right\rceil = 3
\]

So the company needs at least 3 public IPv4 addresses.

## DHCP/NAT Interpretation

DHCP gives internal hosts private addresses dynamically, such as addresses from `10.0.0.0/8` or `192.168.0.0/16`. NAT/PAT maps many internal private addresses to fewer public addresses by changing transport-layer port numbers.

IPv6 reduces the need for NAT because the address space is large enough for devices to have globally routable addresses. However, firewalls and privacy extensions are still needed for security and address management.
