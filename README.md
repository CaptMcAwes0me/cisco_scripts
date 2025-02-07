# Troubleshooting Script  

## Overview  

This Python script is designed specifically for troubleshooting on Cisco Firepower machines. It provides a menu-driven interface for verifying connectivity, analyzing logs, running bandwidth tests, and validating configurations, certificates, and database entries. The script simplifies the troubleshooting process by consolidating common tasks into a single tool.  

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

This script is a menu-driven tool that streamlines troubleshooting on Cisco Firepower machines. It provides various features to verify configurations, test connectivity, analyze logs, and interact with the database. By consolidating these functions into a single tool, it simplifies identifying and resolving issues.  

The script features a simple text-based interface that guides the user through the available options. It requires no additional dependencies beyond Python’s standard library and can be run directly on the Firepower machine.  

### Prerequisites  

- The script is designed to be run on a Cisco Firepower machine.  
- Python 3.x is required.  
- The script uses built-in Firepower tools like `telnet`, `openssl`, and `OmniQuery.pl`.  

### Features  

#### **Firepower Troubleshooting Sections**  

- **Device Information**: Extract and display key details from the system.  
- **Connectivity Tests**: Act as a server or client to verify network reachability.  
- **Bandwidth Testing**: Measure network bandwidth between client and server.  
- **Configuration Validation**: Verify configurations, including `sftunnel.conf` and `sftunnel.json`.  
- **Certificate Validation**: Analyze and display certificate details.  
- **Database Queries**: Interact with tables like `EM_peers`, `ssl_peer`, and `notifications` for troubleshooting.  
- **Log Analysis**: Search logs based on UUID and IP, and export results to a file.  

#### **LINA Troubleshooting Sections**  

This script gathers troubleshooting data from various LINA modules, covering critical system functions:  

- **Blocks** – Analyze block-related configurations.  
- **Cluster** – Display cluster status and related configurations.  
- **Connectivity and Traffic** – Inspect network connectivity and traffic flow.  
- **Failover** – Verify and diagnose failover configurations and status.  
- **Logging and Monitoring** – Extract log data and monitor system events.  
- **NAT** – Display and analyze NAT translations and configurations.  
- **Routing** – Gather routing information from the LINA engine.  
- **VPN** – Check VPN-related configurations and status.  

#### **Data Dump Functionality**  

The script supports data dump functionality for gathering and exporting relevant troubleshooting information. This includes:  

- **LINA Data Dump**: Extracts LINA system data from specific features for debugging and writes it to /var/log/fp_troubleshooting_data/.  

---

## Requirements  

- **Platform**: This script is designed to run exclusively on Cisco Firepower machines.  
- **Python**: Version 3.x or later (only native libraries available).  

---

## How to Use  

1. Copy the script to the Cisco Firepower machine.  
2. Ensure Python 3.x is installed and accessible.  
3. Run the script using:  
   ```bash
   python3 fp_troubleshooting_helper.py
