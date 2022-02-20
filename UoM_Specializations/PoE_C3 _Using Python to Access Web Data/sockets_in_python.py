# %%
# DIALING THE PHONE

import socket
mysocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)  # created the phone
mysocket.connect(('data.pr4e.org', 80))  # diled the phone


# %%

# HTTP protocol : appication layer
# seds get request
# gets the response , and get the data back
# RFC standards
# RFC 2616 : HTTP protocol

# Request
# Telnet
# Metadata
# HTTP : server sends first, we first receive

# %%

# generated the command over HTTP using UTF-8 encoding
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)  # sent the command

# %%

while True:
    data = mysocket.recv(1)  # receving the data 512 characters
    if len(data) < 1:
        break
    print(data.decode(), end='')  # printed what we received

mysocket.close()

# %%
