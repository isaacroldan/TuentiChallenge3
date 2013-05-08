########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 7
#  Isaac Roldán (@saky)
#  
##########################################

#Boozle Game or "Mezcladitos" in spanish.
#Find the best possible score with the given conditions of time and gameboard
#Again, tree search expanding each possible path for each position

#Process: find each possible word for the given board and its score and time.
#Process: Apply the knapsack algorithm to find the best combination of words,  

#IMPORTANT: this implementation is correct, it finds the correct solution but is
#not efficient at all. (almost 4h to solve the submit phase)

import copy

dictionary = []
superArray = []

def main():
	testCases = int(raw_input(""))
	f = open("boozzle-dict.txt",'r')
	global dictionary
	dictionary = f.read().split("\n")
	f.close()
	for i in range(testCases):

		global superArray
		del superArray[:]

		data = raw_input("")
		values = dict(eval(data))
		time = int(raw_input(""))
		rows = int(raw_input(""))
		colu = int(raw_input(""))

		matrix = []

		for i in range(rows):
			row = raw_input("").split(" ")
			matrix.append(row)



		for i in range(rows/5):
		 	for j in range(colu):
				letter = str(matrix[i][j][0])
				value = int(values[letter])


				cm = int(matrix[i][j][2])
				if int(matrix[i][j][1])==1:
					#modo CM
					wmList=1
				else:
					wmList=cm
					cm=1


				history = []
				history.append([i,j])
				findWords(matrix,i,j,rows,colu,values,letter,value*cm,[wmList],history)

		pesos = []
		beneficios = []
		capacidad=time

		for item in superArray:
			#print item
			pesos.append(int(item[2]))
			beneficios.append(int(item[1]))


		newArray = []
		for item in superArray:
			letter = item[0]
			value = item[1]
			peso = item[2]
			newArray.append([letter, peso, value])




		bagged = knapsack01_dp(newArray, capacidad)
		val, wt = totalvalue(bagged)
		print val



def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt
 
    return result


def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)




def findWords(matrix,i,j,rows,colu,values,word,total,wmList,history):

	debug = 0
	caminos = expandir(i,j,rows,colu,history)

	if debug:
		print "\n Caminos:\n"
		for cam in caminos:
		 	print cam
		print "\n History:", history

	for cam in caminos:
		i = cam[0]
		j = cam[1]
		letter = str(matrix[i][j][0])
		

		newWord = copy.deepcopy(word)
		newWord += letter
		if debug: print "WORD: ",newWord

		if not validLetters(newWord): continue

		if debug: print "Valid LETTERS: ",newWord

		value = int(values[letter])

		cm = int(matrix[i][j][2])
		if int(matrix[i][j][1])==1:
			#modo CM
			wm=1
		else:
			wm=cm
			cm=1
			#modo WM
		#wm = int(matrix[i][j][2])

		newTotal = copy.deepcopy(total)
		newTotal+=value*cm
		
		newWm = copy.deepcopy(wmList)
		newWm.append(wm)
		
		newHistory = copy.deepcopy(history)
		newHistory.append([i,j])
	
		if validWord(newWord):
			if debug: print "Valid WORD: ",newWord
			valorFinal = newTotal*max(newWm)+len(newWord)
			time = len(newWord)+1
			addToArray(newWord, valorFinal, time)
		
		findWords(matrix,i,j,rows,colu,values,newWord,newTotal,newWm,newHistory)



def expandir(i,j,rows,colu,history):

	caminos = []

	if i>0 and j>0:
		if [i-1,j-1] not in history:
			cam = [i-1,j-1]
			caminos.append(cam)

	if i>0:
		if [i-1,j] not in history:
			cam = [i-1,j]
			caminos.append(cam)

	if j>0:
		if [i,j-1] not in history:
			cam = [i,j-1]
			caminos.append(cam)

	if i<rows-1:
		if [i+1,j] not in history:
			cam = [i+1,j]
			caminos.append(cam)

	if j<colu-1:
		if [i,j+1] not in history:
			cam = [i,j+1]
			caminos.append(cam)

	if i>0 and j<colu-1:
		if [i-1,j+1] not in history:
			cam = [i-1,j+1]
			caminos.append(cam)

	if i<rows-1 and j<colu-1:
		if [i+1,j+1] not in history:
			cam = [i+1,j+1]
			caminos.append(cam)

	if i<rows-1 and j>0:
		if [i+1,j-1] not in history:
			cam = [i+1,j-1]
			caminos.append(cam)

	return caminos



def validWord(word):
	s=""
	for w in word:
		s+=str(w)
	if s in dictionary:
		return True
	else:
		return False

def validLetters(word):
	s=""
	total = 0
	for w in word:
		s+=str(w)
	
	for d in dictionary:
		if d[:len(s)]==s:
			total += 1
			
	return total


def addToArray(word,value,time):
	for elem in superArray:
		if elem[0]==word and elem[1]>=value:
			return
		elif elem[0]==word and elem[1]<value:
			elem[1]==value
			return

	superArray.append([word, value, time])





if __name__ == '__main__':
	main()