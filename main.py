import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import sys

def scan_http_ports(host="127.0.0.1", port_range=None, ports=None, timeout=3):
    open_ports = []
    
    if port_range:
        start_port, end_port = port_range
        ports_to_scan = range(start_port, end_port + 1)
    elif ports:
        ports_to_scan = ports
    else:
        ports_to_scan = [80, 8080, 8000, 8888, 3000, 5000, 9000]
    
    print(f"HTTP scanning {host}...")
    
    for port in ports_to_scan:
        try:
            response = requests.get(f"http://{host}:{port}/", timeout=timeout)
            print(f"Port {port}: OPEN (HTTP - Status: {response.status_code})")
            open_ports.append(port)
            
        except ConnectionError as e:
            if "Connection refused" in str(e):
                continue
            else:
                print(f"Port {port}: potential open port found")
                open_ports.append(port)
                
                
        except Timeout:
            print(f"Port {port}: TIMEOUT (potential open port found)")
            
        except RequestException:
            continue
    
    return open_ports

if __name__ == "__main__":    
    open_ports = scan_http_ports(port_range=(1, 65535))
    
    print(f"Potential open ports found: {open_ports}")
