# -*- coding: utf-8 -*-
import argparse
import socket


def scan_connection(target_host, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_host, target_port))
        s.send('ViolentPython\r\n')
        results = s.recv(100)
        print "[+] " + str(results)
        print "[+]%d/tcp open" % target_port
        s.close()

    except Exception, e:
        print '[-]%d/tcp closed' + str(e) % target_port


def scan_ports(target_host, target_ports):
    try:
        target_ip = socket.gethostbyname(target_host)
    except Exception, e:
        print "[-] Cannot resolve '%s': Unknown host" % target_host
        print str(e)
        return
    try:
        target_name = socket.gethostbyaddr(target_ip)
        print "\n[+] Scan Results for: " + target_name[0]
    except Exception, e:
        print "\n[+] Scan Results for: " + target_ip + str(e)
        socket.setdefaulttimeout(1)
        for target_port in target_ports:
            print "Scanning port " + target_port
            scan_connection(target_host, target_port)


def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()
    target_host = 'google.com'
    target_port = 80
    scan_ports(target_host, target_port)


if __name__ == '__main__':
    main()
