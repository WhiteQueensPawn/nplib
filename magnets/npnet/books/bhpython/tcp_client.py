import sys
import socket

target_host = "http://www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect the client
    client.connect((target_host, target_port))
    # send some data
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    # receive some data
    response = client.recv(4096)
    print response
except socket.gaierror:
    print "GAIERROR"
    print sys.stderr
    print sys.stdin
    print sys.stdout
