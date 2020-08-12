.PHONY : all clean server
all: readme.html

readme.html: readme.rst
	rst2html readme.rst readme.html

server:
	python3 http_server.py
clean:
	rm -f cgi-bin/hit-count.txt
	rm -f README.html
