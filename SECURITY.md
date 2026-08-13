# Security and sanitization

This is a public portfolio project. Never commit:

- Passwords, tokens, secrets, private keys, or VPN pre-shared keys
- Real public IP addresses or personally identifiable information
- Production device names, domain names, serial numbers, or customer data
- Raw configuration backups that have not been reviewed and sanitized

Use documentation ranges such as `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24` for public-IP examples. Use obvious placeholders for secrets, and load automation credentials from environment variables or a secure secret store.

If a secret is committed accidentally, revoke or rotate it immediately and remove it from Git history before publishing.

