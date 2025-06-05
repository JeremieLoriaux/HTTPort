# HTTP Port Scanner: Functionality, Use Cases, and Comparison with TCP Scanning

## Overview

This report explains how a Python-based HTTP port scanner works, what it reveals, and how it compares to a traditional TCP port scanner. It also discusses why security professionals or attackers might choose one method over the other depending on their objectives.

## What the Code Does

The code defines a function `scan_http_ports()` that attempts to connect to a list or range of ports on a target host using **HTTP GET requests**. It checks whether each port is open and listening for HTTP traffic and logs the result.

### Key Features

- Uses the `requests` library to send HTTP requests to each port.
- Handles common errors such as timeouts and connection refusals.
- Reports the status of each port based on HTTP response or error behavior.
- Returns a list of potentially open ports where HTTP services may be running.

### Code Behavior Summary

```python
requests.get(f"http://{host}:{port}/", timeout=3)
```

This line attempts to connect to a specific port using the HTTP protocol. If the connection succeeds, the server's response (including the HTTP status code) gives further insight into what is running on that port.

## What Is a TCP Port Scanner?

A **TCP port scanner** works at the transport layer. It sends raw TCP connection requests to ports and checks whether the target host **accepts or rejects the connection**.

### Example using Python sockets

```python
import socket
sock = socket.socket()
sock.connect_ex(("192.168.1.1", 80))
```

If the connection succeeds, the port is open. If not, it's closed or filtered. However, it doesn't tell you what kind of service is running on the port.

## HTTP vs. TCP Scanning: Key Differences

| Feature                        | HTTP Port Scanner                     | TCP Port Scanner                      |
|-------------------------------|----------------------------------------|----------------------------------------|
| Protocol Layer                | Application (HTTP)                     | Transport (TCP)                        |
| Can detect web servers?       | Yes                                    | Only if you inspect further            |
| Knows service type            | Yes (HTTP responses)                   | No                                     |
| Returns status codes          | Yes (e.g. 200, 403, 404)               | No                                     |
| Can detect firewalls, proxies | Sometimes (via status or timeout)      | Less obvious                           |
| Speed                         | Slower (full HTTP requests)            | Faster (lightweight TCP handshake)     |
| Use in enumeration phase      | Later (after port discovery)           | Early (broad discovery)                |

## When to Use Each

### TCP Scanning

- Used for **initial reconnaissance** to identify open ports.
- Faster and more general; works across all types of services (SSH, FTP, SMTP, etc.).
- Limited detail: doesn't tell you **what** is running on the open port.


### HTTP Scanning

- Used for **detailed inspection** of ports known (or suspected) to run HTTP-based services.
- Can detect login pages, admin panels, APIs, or misconfigured web apps.
- Helps identify **internal services** that respond differently based on network location.


## Why HTTP Scanning Can Be More Insightful

Unlike TCP scanners, HTTP scanners can reveal how a web application behaves when accessed. It provides context about:

- **Access control** (403 Forbidden, 401 Unauthorized)
- **Resource availability** (404 Not Found, 500 Server Error)
- **Server configuration** (through headers and errors)
- **Firewall or proxy behavior** (timeouts, resets)

### Example Scenario

A system has port `8080` open:

- A TCP scan shows: `"Port 8080 is open"`
- An HTTP scan returns: `403 Forbidden`

**Insight**: A web server is running, but access is restricted. This might be an internal-only admin panel or API.

## Use by Security Professionals and Attackers

### Security Professionals

- Use TCP scans for **broad discovery** during reconnaissance.
- Use HTTP scans to **enumerate web services**, find sensitive endpoints, or identify misconfigurations.
- Use HTTP responses to prioritize risk (e.g., an open dashboard vs. a 404 page).

### Malicious Actors

- Use TCP scans to map attack surfaces.
- Use HTTP scans to find exploitable web apps, vulnerable software, or improperly protected internal tools.
- Analyze HTTP headers for server fingerprinting (e.g., outdated software).

## Final Thoughts

An HTTP port scanner complements a traditional TCP scanner. TCP scanning tells you **what is open**. HTTP scanning tells you **what is running** and **how it behaves**.

In a professional security workflow:

1. Start with TCP scanning (e.g., using `nmap`) to identify open ports.
2. Follow up with HTTP scanning to explore application-level behavior on HTTP/S ports.
3. Use the results to guide manual testing or further automation.

Understanding both layers gives you a more complete view of the system and helps prioritize vulnerabilities more effectively.
