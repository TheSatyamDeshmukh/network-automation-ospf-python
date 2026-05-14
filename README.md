# Network Automation with Python & OSPF

A network monitoring and automation project using Python scripts
on a Linux environment, with a multi-router OSPF topology
designed in Cisco Packet Tracer.

## Project Structure
network-automation-ospf-python/
├── scripts/
│   ├── ping_check.py      # Device status checker
│   ├── ip_scanner.py      # Subnet host scanner
│   └── report_gen.py      # Automated report generator
├── reports/               # Auto-generated network reports
├── topology/              # Packet Tracer screenshots
└── README.md

## Features
- Automated ping monitoring of network devices
- Subnet scanning to discover active hosts
- Report generation saved to file with timestamp
- Cron job configured for every 5 minutes auto-run

## Technologies Used
- Python 3
- Linux (Ubuntu)
- Cisco Packet Tracer (OSPF multi-router topology)
- Git & GitHub

## Network Topology
OSPF Area 0 — 3 Routers, 2 Switches, 3 PCs
- R1: 192.168.1.1 | R2: 192.168.2.1 | R3: 192.168.3.1
- Subnets: 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24

## How to Run
```bash
cd scripts
python3 ping_check.py      # Quick device check
python3 ip_scanner.py      # Scan full subnet
python3 report_gen.py      # Generate full report
```

## Sample Output

=============================================

Network Status Check
2026-05-14 12:31:18
[UP]   VMware Gateway (192.168.233.2)
[UP]   Linux VM (192.168.233.135)
[DOWN] Windows Host (192.168.233.1)
Total: 2 UP | 1 DOWN


## Author
Satyam Deshmukh  — Student | Networking + Python Automation
