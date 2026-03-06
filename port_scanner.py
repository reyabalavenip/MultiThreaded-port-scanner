import socket
import time
from concurrent.futures import ThreadPoolExecutor
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}
target = input("Enter target IP: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

open_ports = 0
print("\nScanning target:", target)
print("----------------------------------")

start_time = time.time()

def scan_port(port):
    global open_ports
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))

        if result == 0:
            service = common_ports.get(port, "Unknown Service")
            print(f"[OPEN] Port {port} --> {service}")
            open_ports += 1

        s.close()

    except:
        pass
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))
end_time = time.time()
print("----------------------------------")
print("\nScan finished.")
print(f"Total open ports found: {open_ports}")
print(f"Scan duration: {round(end_time - start_time, 2)} seconds")