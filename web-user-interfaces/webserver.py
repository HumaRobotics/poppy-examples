#!/usr/bin/python

"""
Implement an HTTP web server in Python that knows how to run server-side
CGI scripts coded in Python;  serves files and scripts from current working
dir;  Python scripts must be stored in webdir\cgi-bin or webdir\htbin;
"""

#~ http://apprendre-python.com/page-python-serveur-web-creer-rapidement

 
import BaseHTTPServer
import CGIHTTPServer
 
PORT = 8888
server_address = ("", PORT)

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
#~ handler.cgi_directories = ["/"]

print "Serveur actif sur le port :", PORT

httpd = server(server_address, handler)
httpd.serve_forever()
