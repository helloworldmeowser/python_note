#Network Technology Note, python has a built-in support for TCP socket
#Remember these three line

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(internet, socket name)
mysock.connect(('data.pr4e.org', 80)) # (host which is domain name, port)
