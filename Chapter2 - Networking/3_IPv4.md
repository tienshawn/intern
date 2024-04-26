# Internet Protocol version Four - IPv4

## Basic Concepts:
- IPv4 addresses are normally expressed in dot-notation xxx.xxx.xxx.xxx where xxx is a value from 0 to 255
- Another way to express them is as a 4-tuple of octets, which is an 8-bit segment since 2⁸=256. Here is the same IPv4 address in both dot-notation and 4-tuple octet.

> 172.217.6.36

> 10101100 11011001 00000110 00100100

## Parts of IPv4:
- Network Prefix:
- Host Identifier:
- Subnet number:

## IPv4 Address Classification:
- There are 5 classes of IPv4 addresses, labeled A through E. The class of the IP address is determined by the first 4 bits.
  - Class A — IP addresses are in this class if their first bit is a 0. In dot-notation, this is the range 0.0.0.0 to 127.255.255.255 . The first 8 bits represent the network prefix and the rest represents the host identifier. For example, 127.42.13.69 has network prefix 127 and host identifier 42.13.69
  - Class B — IP addresses are in this class if their first two bits are 10 . In dot-notation, this is the range 128.0.0.0 to 191.255.255.255 . The first 16 bits represent the network prefix and the rest represent the host identifier. For example, 129.42.13.69 has network prefix 129.42 and host identifier 13.69
  - Class C — IP addresses are in this class if their first three bits are 110 . In dot-notation, this is the range 192.0.0.0 to 223.255.255.255 . The first 24 bits represent the network prefix and the rest represent the host identifier. For example, 196.13.42.69 has network prefix 196.13.42 and host identifier 69
  - Class D — IP addresses are in this class if their first four bits are 1110 . In dot-notation, this is the range 224.0.0.0 to 239.255.255.255 . These addresses are used for multi-casting protocols (ie. when a single packet can be sent to multiple hosts in one action)
  - Class E — IP addresses are in this class if their first four bits are 1111 . In dot-notation, this the range 240.0.0.0 to 255.255.255.255 . These addresses are reserved for future and experimental use

## Reserved IP Addresses:
### Loopback IPs
### Private IPs

## Subnets
### Netmask
### Subnetting through Subnet Masks
### Classless Inter-Domain Routing (CIDR)
### Supernetting Through CIDR