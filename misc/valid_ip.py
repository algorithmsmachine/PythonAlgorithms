def is_valid(str):

	str=str.split(".")

	if len(str) != 4 :
		print("length < 4 ")
		return False

	for i in str:
		octet = int(i)
		if not 0<=octet<=255: 
			print(" octel not in between 0 and 255 ")
			return False

	return True

print(is_valid("0.0.0.0"))
#print(is_valid("altanai"))
#print(is_valid("1.2.3.4"))
