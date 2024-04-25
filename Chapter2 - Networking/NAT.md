# NETWORK ADDRESS TRANSLATION

## Table of contents:

## Basic concepts:
> What is NAT?
- Network Address Transalation (NAT) is a service that operates on a router to connect private network to public network

> Why is NAT?
- An IPv4 address is made up of 32 bits (4 bytes) which gives us a total ~4.2 billion unique IP addresses -> not sufficient.
- NAT is born as a short-term solution, in place of IPv6.

> How is NAT?
- Mapping multiple private addresses inside a local network to a public IP address before transferring the information into the Internet. 

## Types of NAT
###  Static NAT:
- One-to-one internal to public static IP mapping.
- Static NAT requires one public IP Address for each mapping to a private IP Address. 
- A public IP Address cannot be mapped to more than one private IP Address.

### Dynamic NAT:
- Private IP is mapped to public IP based on a pool reserved in the Router's RAM.
- The mapping is not static.
- After NAT timeout is reached (no traffic sent/received during that time), the router take the public IP back.

### NAT Overload:
- Other names: NAPT - Network Address Port Translation, IP Masquerading, NAT with PAT.
- Purpose: allows all PCs within the private network to access the Internet through only one IP Address.
- How it works
> - When a packet from the PC passes through router, the Source IP Address field is changed from private IP to public one.
> - The ports are not changed, unless it is used.


----
# References
- [Network Address Translation (NAT): The What, Why and How Explained](https://blog.davidvarghese.dev/posts/nat-explained/)
- [Configure NAT in Packet Tracer](https://ccnatutorials.in/packet-tracer/configure-nat-in-packet-tracer-a-step-by-step-guide/#:~:text=Step-by-Step%20Guide%20to%20Configure%20NAT%20in%20Packet%20Tracer,7%20Step%207%3A%20Test%20the%20NAT%20Configuration%20)
