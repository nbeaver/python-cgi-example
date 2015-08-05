#! /usr/bin/env python2

import subprocess
import cgi

print "Content-type: text/html"
print ""
date_string = subprocess.check_output("date")
birthday_string = subprocess.check_output("birthday")
print cgi.escape(date_string + '\n' + birthday_string).replace("\n", "\n<br>")
