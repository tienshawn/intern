# Network Address Translation (NAT)

## Definition: NAT

Network Address Translation (NAT) is generally referred to as techniques that allow `N` private (non-globally unique) IP addresses to be mapped to `M` global (globally unique) IP address.

- `N <= M`: The translation is done statically or dynamically by assigning at least one public IP address to each private IP address.
- `N > M`: In this case, a public IP address will be shared between multiple computers. A clear distinction can be achieved by means of port multiplexing. The most common case is `M = 1`, e.g. in private DSL - Digital Subcriber Line connection.

## What are private IP addresses?

Private IP addresses are special address ranges which 

- are released for private use without prior registration
- can be therefore occur in different networks
- For this reason, not clear and for end-to-end addressing between publicly available networks
- Therefore IP packets with private recipient addresses not forwarded by routers on the Internet 

The private address ranges are:

- 10.0.0.0/8
- 172.16.0.0/12
- 169.254.0.0/16
- 192.168.0.0/16

The range 169.254.0.0/16 is used for automatic address assignment (Automatic Private IP addressing):
- If a computer starts without a statically assigned address, it attempts to reach a DHCP server.
- If no DHCP server can be found, the operating system assigns a random address from this address block.
- If the ARP resolution to this address fails then it is assumed that this address is not yet used on the local subnet. Otherwise, another address is selected and the process is repeated.

## NAT Terms:
NAT vs PAT:
- Packet contains a Data Payload, a L4 header (TCP/UDP), and a L3 header (IPv4).
- When a packet passes through the router
  - NAT (Network Addresses Translation) only modifies the L3 header.
  - PAT (Port Addresses Translation) modifies both the L3 and L4 header.

Static vs Dynamic:
- Static: Explicit mapping between PRE-translation and POST-translation
- Dynamic: PRE-translation attributes defined by administrator, POST-translation attributes selected by translation device. 

### Static NAT:
- One-to-one internal to public static IP mapping.
- Static NAT requires one public IP Address for each mapping to a private IP Address. 
- A public IP Address cannot be mapped to more than one private IP Address.

### Static PAT:
- Mapping between an ***IP:Port*** to another ***IP:Port***.
- Makes internal resource ports externally accessible.
- Purpose:
 - Facilitates using Non-Standard Ports.
 - Port Forwarding/ Hole Punching.
 - Multiple Servers can use one Public IP Address.

### Dynamic NAT: (rarely used)
- Private IP is mapped to public IP based on a pool reserved in the Router's RAM.
- The mapping is not static.
- After NAT timeout is reached (no traffic sent/received during that time), the router take the public IP back.

### Dynamic PAT:
- Allows many hosts with Private IPs to share one Public IP.
- Translation Device assures unique IP:Port on the outside; host ~65000 concurrent connection per shared IP. 
- What if traffic was initiated bby the outside host?
  - Traffic is dropped because no translation entry exists.
  - Dynamic PAT is Unidirectional - traffic must be initiated from Inside.

## How doesn NAT work in detail? 

Usually, routers assume the network address translation:

```
    PC1     --------+
192.168.1.1         |         Interface 1: 192.168.1.254 
                              (for home network)
                 Switch ------------ Router ------------ Internet ------- Server
                    |         Interface 2: 131.159.20.19                      185.86.235.241
    PC2     --------+         (for Internet connection)
192.168.1.2
```

- PC1, PC2 and Router can communicate with each other via private IP addresses in the subnet 192.168.1.0/24.
- Router can be reached globally via its public address 131.159.20.19.
- PC1 and PC2 cannot communicate directly with other hosts on the Internet because of their private address.
- Hosts on the Internet can not reach either PC1 or PC2 even if they know PC1 and PC2 are behind Router and Router's global address is known.

PC1 accesses a web page located on the server with the IP address 185.86.235.241

The NAT table of Router is empty at the beginning:

| Local IP Addr | Local Port | Global Port |
|:-------------:|:----------:|:-----------:|
|               |            |             |
|               |            |             |

PC1 sends a packet (TCP SYN) to the server:

| SrcIPAddr | 192.168.1.1    |
|:---------:|:--------------:|
| DstIPAddr | 185.86.235.241 |
| SrcPort   | 2736           |
| DstPort   | 80             |

- PC1 uses its private IP address as the sender address
- The source port is randomly selected by PC1 in the range [1024, 65535] (so called **ephemeral ports**)
- The destination is specified by the Application Layer Protocol (80 = HTTP)

Address translation at Router:

| Local IP Addr | Local Port | Global Port |
|:-------------:|:----------:|:-----------:|
|  192.168.1.1  |     2736   |     2736    |
|               |            |             |

- Router exchanges the sender address with its own global address
- If the source port does not cause a collision in the NAT table, it will be retained
- Router creates a new entry in his NAT table that documents the changes to the package
- Router changes the private IP Addr into public IP Addr

| SrcIPAddr | 131.159.20.19  |
|:---------:|:--------------:|
| DstIPAddr | 185.86.235.241 |
| SrcPort   | 2736           |
| DstPort   | 80             |


The server generates a response:

| SrcIPAddr | 185.86.235.241 |
|:---------:|:--------------:|
| DstIPAddr | 131.159.20.19  |
| SrcPort   | 80             |
| DstPort   | 2736           |

- The server does not know about the address translation and considers Router to be PC1
- The recipient address is therefore the public IP address of Router, the destination port is the source port translated by Router from the previous message.

Router reverses the address translation:

| SrcIPAddr | 185.86.235.241 |
|:---------:|:--------------:|
| DstIPAddr | 192.168.1.1    |
| SrcPort   | 80             |
| DstPort   | 2736           |

- The NAT table is searched for the destination port number in the column Global Port, which is returned to Local Port. The destination IP address of the packet is exchanged for the private IP address of PC1
- The modified packet is forwarded to PC1
- Like the server, PC1 doesn not know about the address translation.

PC2 now also accesses the server:

- PC2 sends a packet (TCP SYN) to the server:
    - By coincidence, PC2 selects the same source port as PC1 (2736)

| SrcIPAddr | 192.168.1.2    |
|:---------:|:--------------:|
| DstIPAddr | 185.86.235.241 |
| SrcPort   | 2736           |
| DstPort   | 80             |

Address translation to Router:

| Local IP Addr | Local Port | Global Port |
|:-------------:|:----------:|:-----------:|
|  192.168.1.1  |     2736   |     2736    |
|  192.168.1.2  |     2736   |     2737    |

- Router notices that there is already an entry for PC1 for local port 2736
- Router creates a new entry in the NAT table, with a random value chosen for the global port (e.g. the original port of PC2 + 1)
- The package from PC2 is modified accordingly and forwarded to the server

| SrcIPAddr | 131.159.20.19  |
|:---------:|:--------------:|
| DstIPAddr | 185.86.235.241 |
| SrcPort   | 2737           |
| DstPort   | 80             |

From the server's point of view, the "Computer" Router has simply established two TCP connections.

A router could include addtional information in the NAT table:

- destination IP address and destination port
- The protocol used (TCP, UDP)
- Your own global IP address (useful if a router has more than one global IP address)

Depending on the stored information, one differentiates between different types of NAT. The same variant discussed (plus an endorsement of the protocol in the NAT table) is called Full Cone NAT.

Other NAT variants:

- Port Restricted NAT
- Address Restricted NAT
- Port and Address Restricted NAT
- Symmetric NAT


---
# References:
- [Network Address Translation (NAT): The What, Why and How Explained](https://blog.davidvarghese.dev/posts/nat-explained/)
- [Configure NAT in Packet Tracer](https://ccnatutorials.in/packet-tracer/configure-nat-in-packet-tracer-a-step-by-step-guide/#:~:text=Step-by-Step%20Guide%20to%20Configure%20NAT%20in%20Packet%20Tracer,7%20Step%207%3A%20Test%20the%20NAT%20Configuration%20)
- [Configuring NAT using nftables](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-configuring_nat_using_nftables)
- [NAT Terminology](https://www.practicalnetworking.net/series/nat/nat-terminology/#:~:text=These%20two%20terms%20designate%20whether%20the%20post-translation%20attributes,packets%20should%20be%20translated%20in%20the%20first%20place.)