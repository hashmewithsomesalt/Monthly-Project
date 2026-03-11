import socket
from concurrent.futures import ThreadPoolExecutor
import time

target = input("Enter the target IP address: ") 
target_ip = socket.gethostbyname(target)
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print(f"\n Scanning {target_ip}")
print("-" * 40)

start_time = time.time()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
            try: 
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"Banner: {banner}")
                else:
                    print("No banner received")
            except:
                print("Could not retrieve banner")
        s.close()
    except:
        pass
with ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan_port, port)
end_time = time.time()
print("-" * 40)
print(f"\nScanning completed in {end_time - start_time:.2f} seconds")