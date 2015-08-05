#! /usr/bin/env python2

import subprocess
import cgi

print "Content-type: text/html"
print ""
date_string = subprocess.check_output("date")
print cgi.escape(date_string)
