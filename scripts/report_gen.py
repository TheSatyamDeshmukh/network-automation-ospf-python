# scripts/report_gen.py
import subprocess
import datetime
import ipaddress
import os

devices = {
     "VMware Gateway":  "192.168.233.2",
    "Linux VM":        "192.168.233.135",
    "Windows Host":    "192.168.233.1",
}

subnets = ["192.168.233.0/24"]

def ping(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        capture_output=True
    )
    return result.returncode == 0

def generate_report():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"../reports/network_report_{timestamp}.txt"

    lines = []
    lines.append("=" * 50)
    lines.append("       NETWORK AUTOMATION REPORT")
    lines.append(f"       Generated: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)

    # Section 1 - Device Status
    lines.append("\n[1] DEVICE STATUS CHECK")
    lines.append("-" * 50)
    up = 0
    down = 0
    for name, ip in devices.items():
        status = "UP  " if ping(ip) else "DOWN"
        if status.strip() == "UP":
            up += 1
        else:
            down += 1
        lines.append(f"  {status}  |  {name:<20} | {ip}")

    lines.append(f"\n  Summary: {up} UP | {down} DOWN")

    # Section 2 - Subnet Scan
    lines.append("\n[2] ACTIVE HOST SCAN")
    lines.append("-" * 50)
    for subnet in subnets:
        lines.append(f"\n  Subnet: {subnet}")
        active = []
        network = ipaddress.IPv4Network(subnet, strict=False)
        for ip in network.hosts():
            ip_str = str(ip)
            if ping(ip_str):
                lines.append(f"    [ACTIVE] {ip_str}")
                active.append(ip_str)
        lines.append(f"  Active in {subnet}: {len(active)} hosts")

    lines.append("\n" + "=" * 50)
    lines.append("             END OF REPORT")
    lines.append("=" * 50)

    # File save karo
    os.makedirs("../reports", exist_ok=True)
    with open(filename, "w") as f:
        f.write("\n".join(lines))

    # Screen pe bhi print karo
    print("\n".join(lines))
    print(f"\n  Report saved: {filename}")

if __name__ == "__main__":
    generate_report()
