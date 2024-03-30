import socket
import time

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8080))
s.listen(10) # 10 is the backlog

http_response = b"""HTTP/1.1 200 OK \r
Content-Length: 10\r

hi there!\n\r\n"""

while True:
    conn, address = s.accept()
    print(str(conn.recv(4096)))
    time.sleep(0.5)
    conn.send(http_response)
    conn.shutdown(socket.SHUT_WR)
    conn.close()