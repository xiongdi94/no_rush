import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('13.75.122.11', 9999))

print(s.recv(1024))
for data in ['airline_data']:
    s.send(str.encode(data))
    result = bytes.decode(s.recv(1024))
    print(result)
s.send(b'exit')
s.close()
