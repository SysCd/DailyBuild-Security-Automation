# DailyBuild — Security & Automation

A practical portfolio of network automation and FortiGate security labs.

## Automation

Python and Netmiko running through the lab VPN to Cisco IOSv routers in Cisco CML.

**Workflow:** Cisco CML → VPN → Python/Netmiko → IOSv routers

- Connects to multiple Cisco routers over SSH
- Runs operational commands across each device
- Collects interface, routing, and version information
- Scales through a YAML device inventory
- Loads credentials securely from environment variables

![Netmiko collecting Cisco IOS output](automation/screenshots/netmiko-output.png)

**Next:** configuration backups → controlled changes → validation → reporting

---

## Security

Hands-on FortiGate labs covering secure edge design, segmentation, policy control, NAT, VPNs, logging, and troubleshooting.

- Secure LAN-to-WAN edge with routing, policy, and source NAT
- Segmented DMZ with controlled inter-zone traffic and VIPs
- Site-to-site IPsec VPN configuration and recovery
- Log-based traffic diagnosis and fault isolation

![Sanitized FortiGate VM dashboard](evidence/fortigate-dashboard-sanitized.png)
