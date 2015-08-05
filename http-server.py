#! /usr/bin/env python2

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/

import BaseHTTPServer
import CGIHTTPServer
import webbrowser
import cgitb; cgitb.enable()

PORT = 8000
script = "test_cgi.py"

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", PORT)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)

url = 'http://localhost:{0}/{1}'.format(PORT, script)

webbrowser.open_new_tab(url)

print "serving at port", PORT

httpd.serve_forever()
