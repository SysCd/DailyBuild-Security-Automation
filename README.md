# DailyBuild — Security & Automation

A practical portfolio of network security and automation labs, centred on FortiGate administration and Python-based network operations.

> **Status:** Active learning project. Labs will be documented as they are built and validated.

The tracks below are learning roadmaps, not a commitment to publish every practice session. Only selected milestone labs will receive full portfolio write-ups.

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

| Day | Lab | Core task |
| ---: | --- | --- |
| 1 | Management | Secure CLI/GUI access; inspect interfaces and configuration |
| 2 | Basic Edge | Configure LAN/WAN addressing |
| 3 | Internet Edge | Add security policy and source NAT |
| 4 | Stateful Firewall | Inspect sessions and return traffic |
| 5 | Policy Control | Control TCP, UDP, ICMP, and specific ports |
| 6 | Troubleshooting | Diagnose broken policy, routing, and NAT |
| 7 | Multi-Zone | Segment networks and control inter-zone traffic |
| 8 | DMZ | Publish a web server with destination NAT/VIP |
| 9 | Objects | Build address and service object groups |
| 10 | Logs | Diagnose traffic from FortiGate logs |
| 11 | Application Control | Apply application control and security profiles |
| 12 | VPN | Build a site-to-site IPsec VPN |
| 13 | VPN Troubleshooting | Break and recover VPN configuration and routing |
| 14 | Consolidation | Rebuild LAN, WAN, policy, and NAT from memory |
| 15 | Enterprise Edge | Combine routing, NAT, policy, DMZ, and logging |
| 16 | Troubleshooting | Find and fix five injected firewall faults |
| 17+ | Repeat and Scale | Build increasingly realistic networks |

## Network automation track

| Day | Lab | Core task |
| ---: | --- | --- |
| 1 | Python and Cisco | SSH to one device with Netmiko |
| 2 | Show Commands | Collect interfaces, routes, and VLANs |
| 3 | Multiple Devices | Loop through a router/switch inventory |
| 4 | Backups | Save running configurations automatically |
| 5 | JSON/YAML Inventory | Store IPs, usernames, and device types |
| 6 | Config Push | Configure interfaces and VLANs with Python |
| 7 | Validation | Verify post-configuration state |
| 8 | Troubleshooting | Handle SSH, authentication, and timeout failures |
| 9 | Parsing | Extract structured data from CLI output |
| 10 | Jinja2 | Generate configurations from templates |
| 11 | Compliance | Check NTP, VLANs, SSH, and interfaces |
| 12 | Reporting | Produce a pass/fail compliance report |
| 13 | Ansible | Run show commands across devices |
| 14 | Ansible Config | Push configuration changes |
| 15 | Consolidation | Rebuild the workflow from scratch |
| 16+ | Portfolio Project | Inventory → backup → change → validate → report |

## Documentation approach

Routine practice does not need a full report. Complete write-ups are reserved for milestone labs that best demonstrate design, implementation, validation, and troubleshooting. Use [LAB_TEMPLATE.md](LAB_TEMPLATE.md) for those selected projects.

## Security and privacy

All examples must be sanitized before they are committed. Real passwords, API keys, private keys, public IP addresses, serial numbers, customer data, and production hostnames do not belong in this repository. See [SECURITY.md](SECURITY.md).

## Planned next steps

- Complete the first FortiGate management-access lab
- Add the first topology diagram and IP plan
- Build a safe Netmiko connection test using environment variables
- Add automated configuration backups and validation
- Expand into Ansible and Jinja2 after the Python foundations are complete
