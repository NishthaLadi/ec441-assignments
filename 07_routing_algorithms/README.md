# Topic 7 — Routing: Dijkstra and Distance Vector

**Artifact type:** Problem + code  
**Course topic:** Routing: Link State/Dijkstra and Distance Vector

## Problem

Consider the weighted network:

| Link | Cost |
|---|---:|
| A-B | 2 |
| A-C | 6 |
| B-C | 1 |
| B-D | 5 |
| C-D | 2 |
| C-E | 4 |
| D-E | 1 |
| D-F | 3 |
| E-F | 2 |

Answer the following:

1. Run Dijkstra's algorithm from source A.
2. Produce the shortest-path table from A.
3. Derive the forwarding table at A.
4. Simulate failure of link C-D.
5. Recompute shortest paths after the failure.
6. Identify which destinations are affected.

## Worked Solution

Initial shortest paths from A:

- A to B: cost 2 via B
- A to C: cost 3 via B-C
- A to D: cost 5 via B-C-D
- A to E: cost 6 via B-C-D-E
- A to F: cost 8 via B-C-D-F or B-C-D-E-F

Forwarding from A uses the next hop on each shortest path. For destinations B, C, D, E, and F, the next hop is B because all shortest paths begin with A-B.

After link C-D fails, paths using C-D must be recomputed. The route from A to D may shift to A-B-D, and routes to E/F may also change depending on total cost.

## Interpretation

Dijkstra represents link-state routing because each router computes paths using a full graph. A link failure can change not only the path to the adjacent node, but also downstream paths whose shortest route depended on that link.
