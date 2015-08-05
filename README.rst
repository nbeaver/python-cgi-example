==========================
Simple python2 cgi script.
==========================

----------
Quickstart
----------

Run this command::

    python2 ./http-server.py

This should open a browser page showing the current date.

----------
Motivation
----------

Most tutorials for python CGI scripts I have found have flaws such as:

- Requiring installation of a web server like ``apache``
  instead of just serving from a local directory using python's ``SimpleHTTPServer``.
- Not opening the browser to the correct page, which is easy with the ``webbrwoser`` package.
- Not explaining the difference between the HTTP header and the HTML.
- Not motivating the CGI concept using examples like the running commands with the ``subprocess`` module.
- Sending plain text instead of HTML.
- Sending a static string instead of dynamic output.
