import socket
import sys
import time

target = input("Enter target IP or hostname:")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    sys.exit()

print(f"\nScanning {target_ip} for open ports...")
print("-" * 40)

start_port = int(input("Enter start port:"))
end_port = int(input("Enter end port:"))

start_time = time.time()

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()
end_time = time.time()

print("-" * 40)
print(f"Scanning completed in {end_time - start_time:.2f} seconds.")