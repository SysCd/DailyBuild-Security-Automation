# DailyBuild — Security & Automation

A practical portfolio of network security and automation labs, centred on FortiGate administration and Python-based network operations.

> **Status:** Active learning project. Labs will be documented as they are built and validated.

## What this repository demonstrates

- FortiGate management, routing, firewall policy, NAT, DMZ, and VPN configuration
- Network topology design and IP addressing plans
- Python and Netmiko automation
- YAML/JSON device inventories
- Configuration backup and show-command collection
- Configuration validation and compliance checks
- Structured troubleshooting with evidence and lessons learned

## Repository map

```text
.
├── fortigate/       # FortiGate lab scenarios and notes
├── automation/      # Python/Netmiko automation projects
├── diagrams/        # Network diagrams and IP plans
├── configs/         # Sanitized example configurations
└── evidence/        # Sanitized screenshots and command output
```

## FortiGate learning path

| Lab | Topic | Status |
| --- | --- | --- |
| 01 | Management access | Planned |
| 02 | Basic edge firewall | Planned |
| 03 | NAT and firewall policy | Planned |
| 04 | DMZ design | Planned |
| 05 | VPN | Planned |

## Automation learning path

| Lab | Topic | Status |
| --- | --- | --- |
| 01 | Netmiko basics | Planned |
| 02 | Configuration backups | Planned |
| 03 | Device inventory | Planned |
| 04 | Controlled configuration push | Planned |
| 05 | Validation and compliance | Planned |

## Lab documentation standard

Each completed lab should include:

1. Objective and scenario
2. Topology and IP plan
3. Configuration steps or automation workflow
4. Validation tests
5. Troubleshooting notes
6. Sanitized evidence
7. Lessons learned

Use [LAB_TEMPLATE.md](LAB_TEMPLATE.md) when starting a new lab.

## Security and privacy

All examples must be sanitized before they are committed. Real passwords, API keys, private keys, public IP addresses, serial numbers, customer data, and production hostnames do not belong in this repository. See [SECURITY.md](SECURITY.md).

## Planned next steps

- Complete the first FortiGate management-access lab
- Add the first topology diagram and IP plan
- Build a safe Netmiko connection test using environment variables
- Add automated configuration backups and validation
- Expand into Ansible and Jinja2 after the Python foundations are complete

