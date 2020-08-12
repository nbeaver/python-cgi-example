==========================
Simple python3 cgi script.
==========================

----------
Quickstart
----------

Clone the repo::

    git clone https://github.com/nbeaver/python-cgi-example

Move into the directory::

    cd python-cgi-example

Run this command::

    python3 ./http_server.py

This should open a browser page showing the current date
and a hit counter that increases each time the page is reloaded.

Modify `<cgi-bin/hit_counter.py>`_ and reload the page to see the effects.

Hit ``Ctrl-C`` to stop the web browser once you are finished.

----------
Motivation
----------

Most tutorials for Python CGI scripts I have seen
have flaws such as:

- Requiring installation of a web server like ``apache``
  instead of just serving from a local directory
  using Python's ``SimpleHTTPServer``.

- Requiring write access to directories like ``/var/www/cgi-bin/``.

- Not opening the browser to the correct page when the server starts.

- Not storing the cgi script in a separate directory
  from the server source code.

- Not providing the code in a convenient bundle to download, run, and modify.

as well as pedagogical flaws such as:

- Not distinguishing the HTTP header from the HTML.

- Sending plain text instead of HTML.

- Sending static HTML instead of dynamic output.

- Sending dynamic output that could be done entirely client-side.

The included `CGI script`_ is a simple hit counter
that writes to a file on disk to store the count.

.. _CGI script: cgi-bin/hit_counter.py

.. note:: This is a pedagogical exercise,
          and is not the best way to implement a hit counter in general.
