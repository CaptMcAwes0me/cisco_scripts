# Troubleshooting Script

## Overview
This Python script is designed specifically for troubleshooting on Cisco Firepower machines. It provides a menu-driven interface for verifying connectivity, analyzing logs, running bandwidth tests, and validating configurations, certificates, and database entries. The script is meant to simplify the troubleshooting process by consolidating common tasks into a single tool.

---

## Table of Contents

- [Overview](#overview)
- [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)

---

## Introduction

The script is a menu-driven tool that simplifies the troubleshooting process on Cisco Firepower machines. It provides a number of features to help verify configurations, test connectivity, analyze logs, and interact with the database. By consolidating these functions into a single tool, it aims to streamline the troubleshooting process and make it easier to identify and resolve issues.

The script is designed to be easy to use, with a simple text-based interface that guides the user through the available options. It requires no additional dependencies beyond Python's standard library and can be run directly on the Firepower machine.

### Prerequisites

- The script is designed to be run on a Cisco Firepower machine.
- Python 3.x is required to run the script.
- The script uses tools like `telnet`, `openssl`, and `OmniQuery.pl` for various operations.

### Features

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
- **Python**: Version 3.x or later.

---

## How to Use

1. Copy the script to the Cisco Firepower machine.
2. Ensure Python 3.x is installed and accessible.
3. Run the script using:
   ```bash
   python3 troubleshooting_script.py
