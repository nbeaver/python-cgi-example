#! /usr/bin/env python2

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# https://docs.python.org/2/library/basehttpserver.html
# https://docs.python.org/2/library/cgihttpserver.html

import BaseHTTPServer
import CGIHTTPServer
import webbrowser

PORT = 8000
script_path = "cgi-bin/hit-counter.py"

server_class = BaseHTTPServer.HTTPServer
handler_class = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", PORT)

httpd = server_class(server_address, handler_class)

url = 'http://localhost:{0}/{1}'.format(PORT, script_path)

webbrowser.open_new_tab(url)

print "serving at", url

httpd.serve_forever()
