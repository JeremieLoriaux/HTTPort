```
 /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$                       /$$    
| $$  | $$|__  $$__/|__  $$__/| $$__  $$                     | $$    
| $$  | $$   | $$      | $$   | $$  \ $$ /$$$$$$   /$$$$$$  /$$$$$$  
| $$$$$$$$   | $$      | $$   | $$$$$$$//$$__  $$ /$$__  $$|_  $$_/  
| $$__  $$   | $$      | $$   | $$____/| $$  \ $$| $$  \__/  | $$    
| $$  | $$   | $$      | $$   | $$     | $$  | $$| $$        | $$ /$$
| $$  | $$   | $$      | $$   | $$     |  $$$$$$/| $$        |  $$$$/
|__/  |__/   |__/      |__/   |__/      \______/ |__/         \___/  

```

## Features

- HTTP-based scanning using real `GET` requests
- Detects open HTTP ports with status codes (e.g., 200, 403, 404)
- Interprets different HTTP response behaviors
- Provides insight beyond just port state (e.g., firewalled vs. web server errors)
- Works on localhost or remote targets
- Custom port range or common HTTP ports (80, 8080, 8000, etc.)
- Timeout control to avoid long delays

---

## Requirements

- Python 3.7+
- Standard library only (`requests` included by default in most setups)

Install manually if needed:

```
pip install requests
```

---

## Usage

Run the scanner directly from the command line:

```bash
python http_scan.py
```

## Example Output

```
HTTP scanning 127.0.0.1...
Port 80: OPEN (HTTP - Status: 200)
Port 3000: OPEN (HTTP - Status: 403)
Port 8000: OPEN (HTTP - Status: 404)
Port 8080: OPEN (HTTP - Status: 401)
Port 8888: TIMEOUT (potential open port found)
Port 9000: No response
```

---

## How It Works

The script sends an HTTP `GET` request to each specified port. If a valid HTTP response is received, it logs the port and the HTTP status code. It handles:

- `ConnectionError`: port likely closed or not serving HTTP
- `Timeout`: service may exist but not responding
- `RequestException`: catch-all for malformed or inaccessible HTTP behavior

This method helps distinguish between:

- **Open ports with actual web services**
- **Filtered ports showing timeouts**
- **Closed ports refusing connections**
- **Ports responding with auth errors or redirects**

---

## HTTP vs. TCP Port Scanning

| Feature         | TCP Scanner              | HTTP Scanner                            |
|----------------|--------------------------|-----------------------------------------|
| Protocol        | TCP layer                | Application (HTTP) layer                |
| Speed           | Very fast (raw socket)   | Slower (real HTTP handshake)           |
| Info returned   | Open/closed/filtered     | HTTP status code, response behavior     |
| Stealth         | Can be stealthy (SYN)    | Not stealthy                            |
| Required libs   | socket, scapy            | requests                                |
| Detection       | Harder with SYN scan     | Easier (more visible in logs)           |

---

## When to Use HTTP Scanning

Security testers and developers might prefer HTTP scanning when:

- You want to detect **running web apps**, not just open ports
- You're trying to fingerprint **web server behavior** (e.g., errors, redirects, auth)
- You suspect a port is open but **firewalled externally** and only accessible internally
- You're debugging **misconfigured reverse proxies or containerized apps**

---

## Example Scenarios

### 1. Testing localhost development servers

```bash
python http_scan.py --host 127.0.0.1 --ports 3000,5000,8000
```

### 2. Checking DMZ/internal app accessibility

Used on a server inside the network to see which ports expose web apps internally but not externally.

### 3. Reconnaissance on pentests

Combine this with a TCP port scan to identify which open ports serve HTTP, and which don't.

---

## Limitations

- Only scans HTTP (not HTTPS)
- No threading (not ideal for large ranges)
- Doesn't parse HTML, only looks for port responses
- No authentication or cookie/session handling

---

## Authors

- [Mihai](https://github.com/mihai-ilie-01)

---

## Disclaimer

This tool is for **authorized security testing and educational use** only. Do not scan systems you do not own or have permission to analyze.


