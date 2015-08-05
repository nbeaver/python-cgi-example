==========================
Simple python2 cgi script.
==========================

----------
Quickstart
----------

Run this command::

    python2 ./http-server.py

This should open a browser page showing the current date and a hit counter that increases each time the page is reloaded.

Modify `<cgi-bin/hit-counter.py>`_ and reload the page to see the effects.

Hit ``Ctrl-C`` to stop the web browser once you are finished.

----------
Motivation
----------

Most tutorials for python CGI scripts I have found have flaws such as:

- Requiring installation of a web server like ``apache`` instead of just serving from a local directory using python's ``SimpleHTTPServer``.

- Requiring write access to directories like ``/var/www/cgi-bin/``.

- Not opening the browser to the correct page when the server is started.

- Not separating the HTTP header and the HTML.

- Sending plain text instead of HTML.

- Sending a static string instead of dynamic output.

- Using examples that could be done client-side with Javascript.

This is an example of a simple hit counter that writes to a file on disk to store the count.

(Not that this is a pedagogical exercise, and is not the best way to implement a hit counter in general.)
