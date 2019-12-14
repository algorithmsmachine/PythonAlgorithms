import socket

class SocketWrapper(object):

	def __init__(self, ip_address, port=8080):
		self.ip_address  = ip_address
		self.port	= port
		#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#s.conect

	def get_details(self,data):
		#import ipdb; ipdb.set_trace()

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip_address , self.port))
		#		data += '\r\n'		

		s.send(data.encode())

		message = ''
		while True:
			return_data = s.recv(50000) # wait for 50000 bytes of datai chunks  for buffer 
			if not return_data :
				break;
			message += return_data.decode('utf8','ignote')
				
		return message

