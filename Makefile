.PHONY : all clean server
all: README.html

README.html: README.rst
	rst2html README.rst README.html

server:
	python2 http-server.py
clean:
	rm -f cgi-bin/hit-count.txt
	rm -f README.html
