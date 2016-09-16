# -*- coding: utf-8 -*-
import requests
import getpass


# store all HTTP status codes in a dict
status_codes = {100: "Continue", 101: "Switching Protocols",
                200: "OK", 201: "Created", 202: "Accepted", 203: "Non-Authoritative Information",
                204: "No Content", 205: "Reset Content", 206: "Partial Content",
                300: "Multiple Choices", 301: "Moved Permanently", 302: "Found",
                303: "See Other", 304: "Not Modified", 305: "Use Proxy", 306: "(Unused)",
                307: "Temporary Redirect",
                400: "Bad Request", 401: "Unauthorized", 402: "Payment Required",
                403: "Forbidden", 404: "Not Found", 405: "Method Not Allowed", 406: "Not Acceptable",
                407: "Proxy Authentication Required", 408: "Request Timeout", 409: "Conflict",
                410: "Gone", 411: "Length Required", 412: "Precondition Failed",
                413: "Request Entity Too Large", 414: "Request-URI Too Long",
                415: "Unsupported Media Type", 416: "Requested Range Not Satisfiable",
                417: "Expectation Failed",
                500: "Internal Server Error", 501: "Not Implemented", 502: "Bad Gateway",
                503: "Service Unavailable", 504: "Gateway Timeout", 505: "HTTP Version Not Supported"}


def github_login():
    # store host and credentials
    host = 'https://api.github.com/user'
    user = 'WhiteQueensPawn'
    phrase = getpass.getpass()
    cred = (user, str(phrase))

    # connect to host and get a response
    r = requests.get(host, auth=cred)

    # output response info to  the console
    print "[+] Host: " + host
    print "[+] Status code: " + str(r.status_code) + " " + status_codes[r.status_code]
    print "[+] Content type: " + str(r.headers['content-type'])
    print "[+] Encoding: " + str(r.encoding)
    print "[+] Text: " + str(r.text)
    print "[+] JSON: " + str(r.json())

    filename = 'response.txt'
    chunk_size = 32

    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


def main():
    github_login()


if __name__ == '__main__':
    main()
