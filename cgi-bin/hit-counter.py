#! /usr/bin/env python2

import subprocess
import cgi
import cgitb
import time
cgitb.enable()

header = "Content-type: text/html\n\n"

date_string = time.strftime('%A, %B %d, %Y at %I:%M:%S %p %Z')

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Current date</title>
</head>
<body>
  {0}
</body>
</html>
""".format(cgi.escape(date_string))

print header + html
