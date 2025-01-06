# Troubleshooting Script

## Overview

This Python script is designed specifically for troubleshooting on Cisco Firepower machines. It provides a menu-driven interface for verifying connectivity, analyzing logs, running bandwidth tests, and validating configurations, certificates, and database entries.

### Features:
- **Device Information**: Extract and display key details from the configuration file.
- **Connectivity Tests**: Act as a server or client to verify network reachability.
- **Bandwidth Testing**: Measure network bandwidth between client and server.
- **Configuration Validation**: Verify the contents of configuration files like `sftunnel.conf` and `sftunnel.json`.
- **Certificate Validation**: Analyze and display certificate details.
- **Database Queries**: Interact with tables like `EM_peers`, `ssl_peer`, and `notifications` for troubleshooting.
- **Log Analysis**: Search logs based on UUID and IP, and export results to a file.

---

## Requirements

- **Platform**: This script is designed to run exclusively on Cisco Firepower machines.
- **Python**: Version 3.x
- **Dependencies**: None beyond Python's standard library.
- **Tools**:
  - `telnet`
  - `openssl`
  - `OmniQuery.pl`

---

## How to Use

1. **Run the Script**:
   ```bash
   python3 fp_troubleshooter.py
