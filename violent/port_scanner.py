import argparse
import socket


def scan_connection(target_host, target_port):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((target_host, target_port))

        s.send("NP Old Masters\r\n")

        results = s.recv(100)

        print "[+]%d/tcp open" % target_port
        print "[+] " + str(results)

        s.close()

    except Exception, e:

        print "[-]%d/tcp closed" % target_port
        print "[-] " + str(e)


def scan_ports(target_host, target_ports):

    try:

        target_ip = socket.gethostbyname(target_host)

    except Exception, e:

        print "[-] Cannot resolve '%s': Unknown host" % target_host
        print "[-] " + str(e)

        return

    try:

        target_name = socket.gethostbyaddr(target_ip)

        print "\n[+] Scan Results for: " + target_name[0]

    except Exception, e:

        print "\n[+] Scan Results for: " + target_ip
        print str(e)

        socket.setdefaulttimeout(1)

        for target_port in target_ports:

            print "Scanning port " + target_port

            scan_connection(target_host, int(target_port))


def main():

    parser = argparse.ArgumentParser()
    parser.parse_args()

    parser.add_argument('-H', '--host', type=str, dest='target_host',
                        help="specify target host")

    parser.add_argument('-p', '--port', type=str, dest='target_port',
                        help="specify target port(s) separated by comma")

    parser.add_argument('-v', '--version', )

    args = parser.parse_args()

    target_host = args.target_host

    target_ports = str(args.target_port).split(', ')

    if target_host is None or target_ports[0] is None:

        print "[-] You must specify a target host and port[s]."

        exit(0)

    scan_ports(target_host, target_ports)


if __name__ == '__main__':
    main()
