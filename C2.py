########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 2
#  Isaac Roldán (@saky)
#  
##########################################

#Comment: not very efficient solution

def main():
	raw_input("")
	fileName = str(raw_input(""))
	raw_input("")
	suggestions = int(raw_input(""))
	raw_input("")
	wordList=[]
	for i in range(suggestions):
		word = raw_input("")
		wordList.append(word)
	print wordList
	dictionary = check(wordList,fileName)

	for key in wordList:
		lista = dictionary[key]
		lista = lista[0:len(lista)-1]
		print key + " -> " + lista 


def check(wordList,fileName):
	f = open(fileName,'r')
	dictionary = {}

	while(1):
		for line in f:
			if line=="":break
			line = line.split("\n")[0]

			for word in wordList:
				chars = set(word)
				if chars.issubset(line):
					if line != word:
						#lista = lista + line + " "
						if word in dictionary:
							dictionary[word] = dictionary[word]+line+" "
						else:
							dictionary[word] = line + " "


	
	return dictionary

if __name__ == '__main__':
	main()