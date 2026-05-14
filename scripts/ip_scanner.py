# scripts/ip_scanner.py
import subprocess
import ipaddress
import datetime

def scan_subnet(subnet):
    print("=" * 45)
    print(f"  Scanning: {subnet}")
    print(f"  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 45)

    active = []
    network = ipaddress.IPv4Network(subnet, strict=False)

    for ip in network.hosts():
        ip_str = str(ip)
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip_str],
            capture_output=True
        )
        if result.returncode == 0:
            print(f"  [FOUND] {ip_str}")
            active.append(ip_str)
        else:
            print(f"  [----]  {ip_str}")

    print("-" * 45)
    print(f"  Active hosts found: {len(active)}")
    return active

if __name__ == "__main__":
    # Apni subnets yahan daalo
    subnets = [
         "192.168.233.0/24"
    ]
    for subnet in subnets:
        scan_subnet(subnet)
        print()
 
