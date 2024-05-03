# NETWORK ADDRESS TRANSLATION

## Table of contents:

## Basic concepts:
> What is NAT?
- Network Address Translation (NAT) is a service that operates on a router to connect private network to public network

> Why does NAT exist?
- An IPv4 address is made up of 32 bits (4 bytes) ~4.2 billion unique IP addresses -> not sufficient.
- NAT is born as a short-term solution in place of IPv6.

> How is NAT?
- Mapping multiple private addresses inside a local network to a public IP address before transferring the information into the Internet. 

## NAT Terms:
### NAT vs PAT:
- Packet contains a Data Payload, a L4 header (TCP/UDP), and a L3 header (IPv4).
- When a packet passes through the router
  - NAT (Network Addresses Translation) only modifies the L3 header.
  - PAT (Port Addresses Translation) modifies both the L3 and L4 header.

### Static vs Dynamic:
- Static: Explicit mapping between PRE-translation and POST-translation
- Dynamic: PRE-translation attributes defined by administrator, POST-translation attributes selected by translation device. Translate private IP in a network into public IP in a reserved pool.

###  Static NAT:
- One-to-one internal to public static IP mapping.
- Static NAT requires one public IP Address for each mapping to a private IP Address. 
- A public IP Address cannot be mapped to more than one private IP Address.

### Static PAT:
- Mapping between an IP:Port to another IP:Port.
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


### NAT Overload:
- Other names: NAPT - Network Address Port Translation, IP Masquerading, NAT with PAT.
- Purpose: allows all PCs within the private network to access the Internet through only one IP Address.
- How it works
> - When a packet from the PC passes through router, the Source IP Address field is changed from private IP to public one.
> - The ports are not changed, unless it is used.

### Other NAT: Policy NAT, Twice NAT,...

## How does NAT work:
- NAT creates a set of IP addresses that were reusable, known as Private IPv4 addresses.
  - 10.0.0.0 /8 (range 10.#.#.#)
  - 172.16.0.0 /12 (range 172.[16-31].#.#)
  - 192.168.0.0 /16 (range 192.168.#.#)

- Remaining IP is Public IP Addresses.
- NAT translates Private IP addresses into Unique Public IP Addresses.


----
# References
- [Network Address Translation (NAT): The What, Why and How Explained](https://blog.davidvarghese.dev/posts/nat-explained/)
- [Configure NAT in Packet Tracer](https://ccnatutorials.in/packet-tracer/configure-nat-in-packet-tracer-a-step-by-step-guide/#:~:text=Step-by-Step%20Guide%20to%20Configure%20NAT%20in%20Packet%20Tracer,7%20Step%207%3A%20Test%20the%20NAT%20Configuration%20)
- [Configuring NAT using nftables](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-configuring_nat_using_nftables)