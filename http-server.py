#! /usr/bin/env python2

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()

PORT = 8000

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", PORT)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()

print "serving at port", PORT
httpd.serve_forever()
