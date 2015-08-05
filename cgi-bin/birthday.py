#! /usr/bin/env python2

import subprocess

print "Content-type: text/html"
print ""
birthday_string = subprocess.check_output("birthday")
print birthday_string
