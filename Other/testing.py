import socket              # Import socket module

s = socket.socket()        # Create a socket object
port = 9008                # Reserve a port for your service.

s.connect(("20.244.104.191", port))
print (s.recv(1024))
s.close                    # Close the socket when done