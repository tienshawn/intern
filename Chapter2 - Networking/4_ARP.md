# Address Resolution Protocol
## Definition: ARP

Address Resolution Protocol (or ARP) is a Link-Layer Addressing, provide a mechanism to translate IP address to link-layer address on the same subnet.

## What is Link-layer address (or MAC Address)
Link-layer address, is usually referred as LAN address, a physical address, or a MAC address, is a address that is associated with each unique interfaces. 
> for the simplicity, the term Link-layer address and MAC address will have the same meaning.

- MAC address is 6 bytes long, giving 2^48 possible MAC addresses. These 6-byte addresses are typically expressed in hexadecimal notation, with each pair of the addresses expressed as a pair of hexadecimal numbers. i.e 1A-23-F9-CD-06-9B

- One thing to note is that each network interface (or each device network adapter) has its own unique and permanent MAC address (though now we can change it through software!?)

> How is that possible?
> - the IEEE manages the MAC address space. When a company want to manufacture adapters, is purchases a chunk of the address space consisting of 2^24 addresses.
> - IEEE allocates the chunk of 2^24 addresses by fixing the first 24 bits of a MAC address and letting the company create unique combinations of the last 24 bits for each adapters. 

## How does Network device use MAC address?
When an adapter wants to send a frame to some destination adapter:
- The sending adapter inserts the destination adapter's MAC address into the frame, then sends to the LAN.
- A switch occasionally broadcast an incoming frame onto all of its interfaces.
- When an adapter receives a frame, it will check the MAC address sent.
- If match, adapter extracts then datagram and passes it to the protocol stack. Else, it will discard the frame.

## What is MAC broadcast address?
- is a special MAC address (FF-FF-FF-FF-FF-FF, for Ethernet and 802.11), used to make all the adapters on the LAN to receive and process the frame.

## How does Address Resolution Protocol work?
Each host and router has an ARP table in its memory, mapping IP addresses to MAC addresses.

The ARP table also contains a time-to-live (TTL) value, indicating when each mapping will be deleted from the table.

|IP Address | MAC Address | TTL |
|:----------:|:-----------:|:---:|
|222.222.222.222| 88-B2-2F-54-1A-0F| 13:30:00|
|222.222.222.223| 5C-66-AB-90-75-B1| 13:52:00|

To obtain the MAC address using ARP:
-  First, the sender constructs a special packet called ARP packet. 
   - ARP packet has several fields, containing the sending and receiving IP and MAC addresses.
   - Both ARP query and response packet have the same format.
   - ARP query packet aim to query all the other hosts and routers on the subnet to determine the MAC address corresponding to the IP address being resolved.

- Then, the adapter encapsulates the ARP packet in a link-layer frame, use the broadcast address for the frame's destination address, and transmits the frame into the subnet.
- Then, each of the ARP modules checks if its IP address matches the destination IP address in the ARP packet.
- The one with a match sends back to the querying host a response ARP packet with the desired mapping.



One thing to note is that ARP is plug-and-play; the ARP table gets built automatically and does not have to be configured by system administrator.

## ARP Packet Structure:
