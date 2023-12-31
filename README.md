# 🌐 DNS Watchdog 🕵️‍♂️

## Overview
**DNS Watchdog** 🐶 is a powerful Python script designed to monitor the reliability of DNS resolution for 🌎 **Google** and 📺 **YouTube** using a set of predefined DNS servers. This tool is indispensable for network administrators and IT professionals for comprehensive DNS server performance analysis.

## Features

- **Predefined DNS Servers** 📡
  - Uses four globally recognized IP addresses, representing different DNS servers.

- **DNS Resolution Testing Function** 🔍
  - `check_dns_resolution(ip)`: Methodically resolves "google.com" and "youtube.com" 50 times each using specified DNS servers.

- **Error Detection and Logging** 🚨
  - Captures and logs any failures in DNS resolution, specifying the failed domain, DNS server IP, and the time of failure.

- **Built-in Delays** ⏲️
  - Incorporates a one-second delay between each test iteration to moderate network request frequency.

## To Run:
1. Clone the repository:
```bash git clone git@github.com:jasonsaini/DNS-Watchdog.git ```
2. Run the script:
```bash python dns_watchdog.py ```


## TODOs 📝
- [ ] Implement `click` library for custom command-line flags.
- [ ] Enable configuration of custom global DNS server IPs.
- [ ] Introduce options for adding custom hosts to test.

## License
This project is licensed under the [MIT License](LICENSE).

---

Keep your network's DNS performance in check with **DNS Watchdog**! 💻🌍🛡️
