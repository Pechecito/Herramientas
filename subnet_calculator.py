import ipaddress
import sys

def calculate_subnet_info(cidr):
    # Convertir la dirección CIDR en un objeto de red IPv4
    network = ipaddress.ip_network(cidr, strict=False)
    
    # Calcular la información requerida
    network_id = network.network_address
    broadcast_address = network.broadcast_address
    netmask = network.netmask
    num_hosts = network.num_addresses - 2  # -2 excluye network y broadcast addresses
    
    # Determinar la clase de la dirección IP
    first_octet = int(str(network_id).split('.')[0])
    if 1 <= first_octet <= 126:
        ip_class = 'A'
    elif 128 <= first_octet <= 191:
        ip_class = 'B'
    elif 192 <= first_octet <= 223:
        ip_class = 'C'
    else:
        ip_class = 'Unknown'
    
    # Mostrar la información
    print(f"Network ID: {network_id}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Netmask: {netmask}")
    print(f"Total Hosts: {num_hosts}")
    print(f"IP Class: {ip_class}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subnet_calculator.py <CIDR>")
        sys.exit(1)
    
    cidr = sys.argv[1]
    calculate_subnet_info(cidr)

