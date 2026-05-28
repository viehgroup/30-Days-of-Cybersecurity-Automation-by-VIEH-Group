# Day 04 - DNS Lookup Tool

A simple Python-based DNS lookup tool that retrieves important DNS records for a target domain.

---

## Features

- Fetch A records
- Retrieve MX records
- Get NS records
- Beginner-friendly implementation
- Simple command-line interface

---

## Technologies Used

- Python
- dnspython

---

## Installation

```bash
git clone https://github.com/<url>
cd filename
```

Install dependencies:

```bash
pip install dnspython
```

---

## Usage

```bash
python dns_lookup.py
```

Enter a domain name when prompted.

Example:

```text
example.com
```

---

## Example Output

```text
Enter Domain: example.com

A Records:
93.184.216.34

MX Records:
0 .

NS Records:
a.iana-servers.net
b.iana-servers.net
```

---

## What You Will Learn

- DNS fundamentals
- DNS record enumeration
- Python automation
- Domain intelligence gathering

---

## Challenge Task

Try improving this project by adding:

- TXT record lookup
- Subdomain discovery
- Reverse DNS lookup
- Export results to a file

---

## Disclaimer

This project is intended for educational and authorized security testing purposes only.

---

# 30 Days of Cybersecurity Automation by VIEH Group

Building practical cybersecurity tools
