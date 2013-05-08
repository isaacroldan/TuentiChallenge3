########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 14
#  Isaac Roldán (@saky)
#  
##########################################

#We have 13 encrypted texts, all with the same key
#This file already has the final encryption key

#In C14b.py a html file is generated where we can see each text combination
#Is important to know that a XOR of a LETTER with a SPACE will uppercase or lowercase it, so we
#can start guessing where the spaces are and from there, try to deduce the encrypted text and
#find the key. IN the HTML we can see all combinations, and deduce some spaces and letters


import binascii

def main():

	mensaje = "0x"+raw_input("")
	clave = "0x15944d6464b76d60db32fc723f737b9971f98d0cf061e5fce87a723f89ad78c7c9f864bdbaed7477c821b103172eaed934ed1ac39278076ec1d171a07aefacf1648a257e9950dbe3c76a076723e5483acf43a1b7655a83c0b5fd9c4a1cefbed23934edb3852584a2d7dd56557e76ecd0bb52d4674d5174ec0ee30067ad"
	descifrado = hex(eval(mensaje)^eval(clave))
	print binascii.unhexlify(str(descifrado)[2:-1])


if __name__ == '__main__':
	main()