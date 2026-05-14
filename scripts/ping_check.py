# scripts/ping_check.py
import subprocess
import datetime

# Tumhara Packet Tracer network (ya real network)
devices = {
    
    "VMware Gateway":  "192.168.233.2",
    "Linux VM":        "192.168.233.135",
    "Windows Host":    "192.168.233.1",
}

def ping_device(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        capture_output=True
    )
    return result.returncode == 0

def main():
    print("=" * 45)
    print("   Network Status Check")
    print(f"   {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 45)

    up_count = 0
    down_count = 0

    for name, ip in devices.items():
        status = ping_device(ip)
        if status:
            print(f"  [UP]   {name} ({ip})")
            up_count += 1
        else:
            print(f"  [DOWN] {name} ({ip})")
            down_count += 1

    print("-" * 45)
    print(f"  Total: {up_count} UP | {down_count} DOWN")
    print("=" * 45)

if __name__ == "__main__":
    main()
