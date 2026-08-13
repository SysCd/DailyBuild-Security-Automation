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

## Firewall lab track — FortiGate

| Day | Scenario | Layout | Core task | Done? |
| ---: | --- | --- | --- | :---: |
| 1 | Management | Mac → FortiGate | Access CLI + GUI; inspect interfaces/config | No |
| 2 | Basic Edge | Client → FortiGate → WAN | Configure LAN/WAN interfaces and addressing |  |
| 3 | Internet Edge | Client → FortiGate → Internet | Security policy + source NAT |  |
| 4 | Stateful Firewall | Client → FortiGate → Server | Inspect sessions and understand return traffic |  |
| 5 | Policy Control | LAN → FortiGate → WAN | Allow/deny TCP, UDP, ICMP, and specific ports |  |
| 6 | Troubleshooting | Reuse Day 5 | Break policy, routing, and NAT; diagnose each |  |
| 7 | Multi-Zone | Users + Servers → FortiGate | Separate networks and control inter-zone traffic |  |
| 8 | DMZ | LAN + DMZ + WAN | Publish web server using destination NAT/VIP |  |
| 9 | Objects | Reuse Day 8 | Address/service objects and groups |  |
| 10 | Logs | Reuse topology | Diagnose traffic entirely from FortiGate logs |  |
| 11 | Application Control | LAN → Internet | App control + security profiles |  |
| 12 | VPN | HQ ↔ Branch | Site-to-site IPsec |  |
| 13 | VPN Troubleshooting | Reuse Day 12 | Break phase/config/routes and recover |  |
| 14 | Consolidation | Rebuild | Rebuild LAN/WAN/policy/NAT from memory |  |
| 15 | Enterprise Edge | Users + Servers + DMZ | Combine routing, NAT, policies, and logging |  |
| 16 | Troubleshooting | Reuse Day 15 | Inject five firewall faults and fix them |  |
| 17+ | Repeat/Scale | New scenarios | Build increasingly realistic networks |  |

## Network automation track

| Day | Lab | Core task | Done? |
| ---: | --- | --- | :---: |
| 1 | Python → Cisco | SSH to one device with Netmiko |  |
| 2 | Show Commands | Collect `show ip interface brief`, routes, and VLANs |  |
| 3 | Multiple Devices | Loop through router/switch inventory |  |
| 4 | Backups | Automatically save running configs |  |
| 5 | JSON/YAML Inventory | Store IPs, usernames, and device types |  |
| 6 | Config Push | Configure interfaces/VLANs using Python |  |
| 7 | Validation | Verify changes after configuration |  |
| 8 | Troubleshooting | Handle failed SSH/authentication/timeouts |  |
| 9 | Parsing | Extract useful data from CLI output |  |
| 10 | Jinja2 | Generate configurations from templates |  |
| 11 | Compliance | Check NTP, VLANs, SSH, interfaces, etc. |  |
| 12 | Report | Produce pass/fail compliance report |  |
| 13 | Ansible | Run show commands across devices |  |
| 14 | Ansible Config | Push configuration changes |  |
| 15 | Consolidation | Rebuild automation workflow from scratch |  |
| 16+ | Portfolio Project | Inventory → backup → change → validate → report |  |

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
