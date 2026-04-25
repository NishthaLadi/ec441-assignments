# EC441 Networking Portfolio — Topics 1–9

This repository is organized by topic rather than by week. Each topic folder contains:

- `README.md`: artifact write-up with an elaborate calculation-based problem, worked solution, and interpretation
- `solution.py`: runnable Python code for simulation, visualization, or verification
- `outputs/`: generated plots after running the code

## Course requirement coverage

| Topic | Artifact Type | Network Layer Coverage |
|---|---|---|
| 01 Information Theory | Problem + Code | Conceptual/Application foundation |
| 02 Physical Layer | Problem + Code | Physical |
| 03 Link Layer Error Control | Problem + Code | Data Link |
| 04 Multiple Access | Problem + Simulation | Data Link |
| 05 Ethernet, Switching, ARP | Problem + Simulation | Data Link |
| 06 Reliable Data Transfer | Problem + Simulation | Transport |
| 07 Routing Algorithms | Problem + Code | Network |
| 08 Network Layer Subnetting | Report + Code | Network |
| 09 IPv4, IPv6, DHCP, NAT | Problem + Simulation | Network |

Topic 10, the lab/final project, can be added later as:

```text
10_tcp_tools_applications_lab/
├── README.md
├── lab_report.md
├── ping_analysis.py
├── tcp_client.py
├── tcp_server.py
└── screenshots/
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
pip install -r requirements.txt
```

Then run any topic script:

```bash
python 01_information_theory/solution.py
```

## Generative AI usage

I used generative AI to help brainstorm calculation-heavy networking problems and design simulations. I reviewed and edited the outputs for correctness, clarity, and alignment with course topics.
