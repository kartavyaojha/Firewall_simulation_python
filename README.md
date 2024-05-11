# Python_projects

## Overview

This Python script is designed to simulate a firewall rule checker. It generates random IP addresses and checks them against predefined firewall rules to determine the action to take.

## Features
- **Login Functionality**: Users are prompted to log in with a predefined username and password ("admin").
- **IP Address Generation**: Random IP addresses in the range of "192.168.1.0" to "192.168.1.20" are generated.
- **Firewall Rule Check**: Each generated IP address is checked against predefined firewall rules to determine the action (allow or block).
- **Random Number Generation**: Alongside IP addresses, a random number between 0 and 9999 is generated for each IP.
- **Security Alert**: If an IP address is blocked, a security alert is printed.

## Usage
1. **Login**: Enter the username and password when prompted. The default username and password are both "admin".
2. **Execution**: Run the script. It will generate random IP addresses, check them against firewall rules, and display the result.
3. **Output**: The script will print the IP address, the action taken (allow or block), and the randomly generated number. If an IP address is blocked, a security alert will be displayed.

## Predefined Firewall Rules
- IP addresses "192.168.1.4", "192.168.1.3", "192.168.1.8", and "192.168.1.9" are blocked by default.

## File Structure
- **firewall_checker.py**: The main Python script containing the firewall rule checker functionality.
- **README.md**: This file, providing an overview, features, usage instructions, and other relevant information about the script.

## Requirements
- Python 3.x
- Random module (included in Python standard library)

## Contributors
- Kartavya Ojha
