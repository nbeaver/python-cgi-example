#! /usr/bin/env python2

import subprocess
import cgi

print "Content-type: text/html"
print ""
birthday_string = subprocess.check_output("birthday")
print cgi.escape(birthday_string).replace("\n","<br>\n")
