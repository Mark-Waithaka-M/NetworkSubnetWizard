def calculate_subnet(ip_cidr):
    ip, cidr = ip_cidr.split('/')
    cidr = int(cidr)
    
    total_ips = 2 ** (32 - cidr)
    usable_ips = total_ips - 2
    
    network_parts = ip.split('.')
    network = '.'.join(network_parts[:3])
    host = int(network_parts[3])
    subnet_mask = ".".join(["255"] * (cidr // 8) + [str(256 - 2**(8 - cidr % 8))])
    
    ip_range_start = f"{network}.{host + 1}"
    ip_range_end = f"{network}.{host + usable_ips}"
    
    return total_ips, usable_ips, subnet_mask, ip_range_start, ip_range_end

ip_cidr = input("Enter IP address with CIDR notation (e.g. 192.168.100.1/24): ")
total_ips, usable_ips, subnet_mask, ip_range_start, ip_range_end = calculate_subnet(ip_cidr)

print(f"Total IPs: {total_ips}")
print(f"Usable IPs: {usable_ips}")
print(f"Subnet Mask: {subnet_mask}")
print(f"IP Range: {ip_range_start} - {ip_range_end}")
