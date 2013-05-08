########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 6
#  Isaac Roldán (@saky)
#  
##########################################

#INFO: You are in an ice-cave like the ones in the pokemon games
# You have to find the min time necessary to scape.
# The solution expands a tree with each possible path in each iteration (avoiding loops)

import copy

superArray = []

def main():
	testCases = int(raw_input(""))
	for i in range(testCases):

		global superArray
		del superArray[:]	
		data = raw_input("")
		data = data.split(" ")

		w = int(data[0])
		h = int(data[1])
		speed = int(data[2])
		time = int(data[3])

		matrix = []

		for row in range(h):
			string = raw_input("")
			str2 = ""
			flag=0
			for c in string:
				if c=="#": str2+="#"
				elif c=="X": str2+="X"
				elif c=="O": str2+="O"
				elif flag==0:
					str2+="."
					flag=1
				else:
					flag=0

			matrix.append(str2)

		fI,cI = findInit(matrix)
		fS,cS = findExit(matrix)
		history=[]
		history.append([fI,cI])
		findPath(matrix, fI, cI, fS, cS,w,h,speed,time,[fI,cI],history,0)
		if len(superArray)>0:
			print min(superArray)


#Recursive method to find the optimal path
def findPath(matrix,fI,cI,fS,cS,w,h,speed,time,anterior,history,coste):


	if fI==fS and cI==cS:
	#	print "found! -> ",int(round(coste))
		addToArray(int(round(coste)))
		return

	#Get each possible path from the current position.
	caminos = expand(matrix,fI,cI,h,w,anterior)
	for camino in caminos:
		#We save the positions history to avoid loops
		newHistory=copy.deepcopy(history)

		if [camino[1],camino[2]] in history:
			continue #loop detected, continue with the next iteration
		else:
			newHistory.append([camino[1],camino[2]])

		lon = camino[0]
		aux = lon/float(speed)+time
		newCoste = copy.deepcopy(coste)
		newCoste = newCoste + aux

		if len(superArray)>0:
			if newCoste>min(superArray):
				continue
			#if newCoste>(h*w): continue

		findPath(matrix,camino[1],camino[2],fS,cS,w,h,speed,time,[fI,cI],newHistory,newCoste)


def addToArray(total):
	global superArray
	superArray.append(total)


def expand(matrix,fI,cI,h,w,anterior):
	if matrix[fI][cI]=="O":
		return [0,fI,cI]


	caminos = []
	for i in range(fI,-1,-1):
		if matrix[i][cI]=="#":
			if [i+1,cI]!=anterior:
				camino=[fI-(i+1),i+1,cI]
				if fI-(i+1)>0:
					caminos.append(camino)
				break
			else:
				break
		if matrix[i][cI]=="O":
			camino=[fI-i,i,cI]
			caminos.append(camino)
			break

	for i in range(fI,h):
		if matrix[i][cI]=="#":
			if [i-1,cI]!=anterior:
				camino=[i-1-fI,i-1,cI]
				if i-1-fI>0:
					caminos.append(camino)
				break
			else:
				break
		if matrix[i][cI]=="O":
			camino=[i-fI,i,cI]
			caminos.append(camino)
			break

	for i in range(cI,-1,-1):
		if matrix[fI][i]=="#":
			if [fI,i+1]!=anterior:
				camino=[cI-(i+1),fI,i+1]
				if cI-(i+1)>0:
					caminos.append(camino)
				break
			else:
				break
		if matrix[fI][i]=="O":
			camino=[cI-i,fI,i]
			caminos.append(camino)
			break


	for i in range(cI,w):
		if matrix[fI][i]=="#":
			if [fI,i-1]!=anterior:
				camino=[i-1-cI,fI,i-1]
				if i-1-cI>0:
					caminos.append(camino)
				break
			else:
				break
		if matrix[fI][i]=="O":
			camino=[i-cI,fI,i]
			caminos.append(camino)
			break

	return caminos


def findExit(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j]=="O":
				return i,j


def findInit(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j]=="X":
				return i,j



if __name__ == '__main__':
	main()