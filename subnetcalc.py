#!/usr/bin/env python3
import ipaddress, sys

def info(cidr):
    net = ipaddress.ip_network(cidr, strict=False)
    hosts = list(net.hosts())
    first = hosts[0] if hosts else net.network_address
    last  = hosts[-1] if hosts else getattr(net, "broadcast_address", net.network_address)
    return {
        "version": net.version,
        "network": str(net.network_address),
        "broadcast": str(getattr(net, "broadcast_address", "")),
        "netmask": str(net.netmask),
        "hostmask": str(net.hostmask),
        "first_host": str(first),
        "last_host": str(last),
        "size": net.num_addresses
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: subnetcalc <CIDR>  e.g., 192.168.1.10/24 or 2001:db8::1/64")
        sys.exit(1)
    for k, v in info(sys.argv[1]).items():
        print(k + ": " + str(v))
