"""IPv4 subnet calculator; runs offline with Python standard library."""
import ipaddress
import sys


def describe(cidr):
    interface = ipaddress.IPv4Interface(cidr)
    network = interface.network
    # ipaddress treats both endpoints of /31 and the /32 address as hosts.
    count = network.num_addresses if network.prefixlen >= 31 else network.num_addresses - 2
    first = network.network_address if network.prefixlen >= 31 else network.network_address + 1
    last = network.broadcast_address if network.prefixlen >= 31 else network.broadcast_address - 1
    return {
        "ip": str(interface.ip), "network": str(network),
        "mask": str(network.netmask), "broadcast": str(network.broadcast_address),
        "first_host": str(first), "last_host": str(last), "host_count": count,
    }


if __name__ == "__main__":
    try:
        for key, value in describe(sys.argv[1] if len(sys.argv) > 1 else "192.168.10.70/26").items():
            print("{}: {}".format(key, value))
    except (ValueError, ipaddress.AddressValueError) as error:
        sys.exit("Invalid IPv4 CIDR: {}".format(error))
