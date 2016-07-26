import socket

# create a dictionary of common ports
ports = {
    'echo': 7, 'ftp': 20, 'ftp_cmd': 21, 'ssh': 22, 'telnet': 23,
    'smtp': 25, 'wins': 42, 'whois': 43, 'dns': 53, 'http': 80,
    'https': 443,
    'np': 3333,
}

# set host address
host = '0.0.0.0'


# create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# connect to a host
s.connect((host, ports['http']))
