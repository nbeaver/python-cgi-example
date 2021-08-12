#! /usr/bin/env python3

import html
import cgitb
import time
import os
cgitb.enable()

hit_count_path = os.path.join(os.path.dirname(__file__), "hit-count.txt")

if os.path.isfile(hit_count_path):
    with open(hit_count_path) as fp:
        hit_count_str = fp.read()
        try:
            hit_count = int(hit_count_str)
        except ValueError:
            hit_count = 0
    hit_count += 1
else:
    hit_count = 1

with open(hit_count_path, 'w') as fp:
    fp.write(str(hit_count))

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
  <p>
  Date: {0}
  </p>
  <p>
  Hit count: {1}
  </p>
</body>
</html>
""".format(html.escape(date_string), html.escape(str(hit_count)))

print(header + html)
