########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 3
#  Isaac Roldán (@saky)
#  
##########################################

#We have to reorder a list of phrases depending on the first character of each one.

import re

def main():
	testCases = int(raw_input(""))
	for i in range(testCases):
		line = str(raw_input(""))
		result = orderLine(line)
		print result

def orderLine(line):

	#Any phrase that starts with a ".", "<" or ">"
	frases = re.findall("[\.<>](?:[a-zA-Z0-9,]+[ ]+)+[a-zA-Z0-9,]+",line)

	flag=0
	for i in range(len(frases)):
		#If the phrase starts with a "<" it is a flashback and should be put in his right time
		#We move to a previous position until we reach the first element or until we find the
		#same phrase in a previous position
		if frases[i][0]=="<":
			frases[i], frases[i-1] = frases[i-1], frases[i]
			for j in range(i-1,1,-1):
				if frases[j][1:]==frases[j-1][1:]: 
					newFrase = "*"+frases[j][1:]
					newFrase2 = "*"+frases[j-1][1:]
					frases[j]=newFrase
					frases[j-1]=newFrase2
					break
				else:
					flag=1
					frases[j], frases[j-1] = frases[j-1], frases[j]


	#After sorting, find if there are two equal and consecutive phrases. Keep just one in the new Array
	newLista = []
	for i in range(len(frases)):
		if i==0:
			newLista.append("."+frases[i][1:])
		else:
			if frases[i][1:]!=frases[i-1][1:]:
				newLista.append("."+frases[i][1:])

	#Now, If there is a phrase duplicated, then is an invalid case.
	if duplicates(newLista):
		return "invalid"
	else:
		if flag: #If there are more than 1 posible solution (i.e. a phrase has been moved more than once)
			return "valid"
		else:
			newLista = ','.join(map(str, newLista))
			newLista = newLista.replace('.','').replace('>','').replace('*','')
			return newLista




def duplicates(lst):
	for item in lst:
		concur = [i for i, x in enumerate(lst) if x == item]
		if len(concur)>1:
			return 1	
	return 0


if __name__ == '__main__':
	main()