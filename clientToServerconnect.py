import socket
s = socket.socket()
s.connect(("93.184.216.34",80))
s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
print(str(s.recv(4096)))
