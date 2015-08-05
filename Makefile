.PHONY : all clean server
all: README.html

README.html: README.rst
	rst2html README.rst README.html

server:
	python2 http-server.py
clean:
	rm --force cgi-bin/hit-count.txt
	rm --force README.html
