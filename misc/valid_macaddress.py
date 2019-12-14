class Macadress(object):

	def is_valid(self):
		str = self.macaddress
		str=str.split(":")

		if len(str) != 6 :
			print("Mac address length annot be  < 6 ")
			return False

		for i in str:
			print( " inspecting subpart " + i )

			if 0>len(i)>2 : 
				print(" length not greater than or less than equal to 2 ")
				return False
 
			for j in i :
				print(" inspecting " + j )

				if not j.isdigit and (j>"f" or j<="a"): 
					print("  not a digit and still not between A and F")
					return False

				if not j.isdigit() : 
					print(" not a digit")
					return False

		return True

	def __init__ (self, macaddress):
		self.macaddress = macaddress

	def get_macadress(self):
		return self.macaddress

m = Macadress("d0:81:7a:c2:3c:5a")


