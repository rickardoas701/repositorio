#!/usr/bin/python
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(3, gpio.OUT)
gpio.output(3, False)
gpio.setup(5, gpio.OUT)
gpio.output(5, False)
gpio.setup(7, gpio.OUT)
gpio.output(7, False)
gpio.setup(11, gpio.OUT)
gpio.output(11, False)
try:
	from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
except:
	from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
try:
	from urlparse import urlparse
	from urlparse import urlparse, parse_qs
except:
	from urllib.parse import urlparse, parse_qs

import os
port = int(os.environ.get("PORT", 5000))	
PORT_NUMBER = port




es=0
def leds(path):
	global es
	try:
		cmd,val=path.split('_')
		
	except:
		cmd=''
	#if cmd=='/led1':
	#	if es==0:
	#		print 'enciende led1'
	#		gpio.output(3,True)
	#		es=1
	#	else:
	#		gpio.output(3,False)
	#		print 'apaga led1'
	#		es=0
    if cmd=='/led1':
		if val=='ON':
			gpio.output(3,True)
			print 'enciende led1'
		if val=='OFF':
			gpio.output(3,False)
			print 'apaga led1'
	if cmd=='/led2':
		if val=='ON':
			gpio.output(5,True)
			print 'enciende led2'
		if val=='OFF':
			gpio.output(5,False)
			print 'apaga led2'                
	if cmd=='/led3':
		if val=='ON':
			print 'enciende led3'
			gpio.output(7,True)
		if val=='OFF':
			print 'apaga led4'
			gpio.output(7,False)
	if cmd=='/led4':
		if val=='ON':
			print 'enciende led4'
			gpio.output(11,True)
		if val=='OFF':
			print 'apaga led4'  
			gpio.output(11,False)  









class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		
		if self.path=="/":  #127.0.0.1:5000/
			self.path="/index.html" #127.0.0.1:5000/index.html
		
		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				data=f.read()
				
				try:
					self.wfile.write(data)
				except:
					self.wfile.write(bytes(data, 'UTF-8'))
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('0.0.0.0', PORT_NUMBER), myHandler)
	print ('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()
	