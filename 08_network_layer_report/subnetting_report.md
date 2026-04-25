# Subnetting and CIDR Optimization Report

## 1. Introduction

Efficient IP address allocation is essential in modern networking, especially given the limitations of IPv4 address space. Poor subnet design can lead to excessive address wastage, inefficient routing, and scalability issues.

This report explores the use of:
- CIDR (Classless Inter-Domain Routing)
- VLSM (Variable Length Subnet Masking)

to allocate IP addresses efficiently across multiple departments with varying requirements.

---

## 2. Problem Statement

We are given the base network:

10.20.0.0/16

The organization requires subnet allocation for the following departments:

| Department   | Required Hosts |
|-------------|--------------|
| Engineering | 900 |
| Research    | 420 |
| Operations  | 180 |
| HR          | 75 |
| Guest WiFi  | 50 |

---

## 3. Methodology

### Approach
We use VLSM to allocate subnets based on actual host needs:

1. Sort departments by descending host requirements  
2. Allocate largest subnets first  
3. Ensure proper CIDR alignment  
4. Minimize unused IPs  

### Subnet Formula

2^n - 2 >= Required Hosts

Where:
- n = number of host bits  
- Subnet prefix = 32 - n

---

## 4. Subnet Allocation Results

| Department   | CIDR | Network       | First Usable | Last Usable  | Broadcast     | Capacity | Wasted |
|-------------|------|--------------|-------------|-------------|--------------|----------|--------|
| Engineering | /22  | 10.20.0.0    | 10.20.0.1   | 10.20.3.254 | 10.20.3.255  | 1022     | 122    |
| Research    | /23  | 10.20.4.0    | 10.20.4.1   | 10.20.5.254 | 10.20.5.255  | 510      | 90     |
| Operations  | /24  | 10.20.6.0    | 10.20.6.1   | 10.20.6.254 | 10.20.6.255  | 254      | 74     |
| HR          | /25  | 10.20.7.0    | 10.20.7.1   | 10.20.7.126 | 10.20.7.127  | 126      | 51     |
| Guest WiFi  | /26  | 10.20.7.128  | 10.20.7.129 | 10.20.7.190 | 10.20.7.191  | 62       | 12     |

---

## 5. Address Utilization Analysis

Total wasted usable IPs: 349

### Observations
- Larger subnets (Engineering) waste more absolute addresses  
- Smaller subnets (Guest WiFi) are more efficient  
- VLSM significantly reduces waste compared to fixed subnetting  

---

## 6. Visualization

### Subnet Allocation Efficiency
(See outputs/subnet_allocation_efficiency.png)

### Wasted Addresses
(See outputs/subnet_waste.png)

---

## 7. Routing and Aggregation

Instead of multiple routes:

10.20.0.0/22  
10.20.4.0/23  
10.20.6.0/24  
10.20.7.0/25  
10.20.7.128/26  

We can aggregate into:

10.20.0.0/21

### Benefits
- Reduced routing table size  
- Faster lookup  
- Improved scalability  

---

## 8. Tradeoffs

| Factor | Tradeoff |
|------|--------|
| Large subnets | More wasted IPs |
| Small subnets | More routing entries |
| CIDR aggregation | Less granularity |
| VLSM | More complex design |

---

## 9. Key Insights

- Address allocation is discrete, leading to unavoidable waste  
- VLSM minimizes waste but cannot eliminate it  
- CIDR improves routing efficiency significantly  
- There is a tradeoff between utilization and routing simplicity  

---

## 10. Conclusion

This report demonstrates that:

- VLSM enables efficient subnet allocation tailored to real needs  
- CIDR enables route aggregation, improving scalability  
- Larger departments introduce unavoidable inefficiencies due to binary subnet sizing  

Overall, careful subnet design is critical for balancing:
- address efficiency  
- routing performance  
- network scalability  
