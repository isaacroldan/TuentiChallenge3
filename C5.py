########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 5
#  Isaac Roldán (@saky)
#  
##########################################

#Info: "Snake" like game. Find the max score we can get with the given conditions.


import copy

superArray=[0]
sX =0
sY=0
media = 0

def main():
	testCases = int(raw_input(""))
	for i in range(testCases):
		size = str(raw_input("")).split(",")
		global superArray
		del superArray[:]		
		superArray.append(0)
		init = str(raw_input("")).split(",")
		iX = int(init[0])
		iY = int(init[1])
		time = int(raw_input("")) #time available
		gems = int(raw_input("")) #number of gems in the game
		positions = raw_input("")
		positions=positions.split("#")
		matrix = [["0" for i in range(int(size[0]))] for j in range(int(size[1]))]
		
		
		
		
		global sX
		sX = int(size[0])
		global sY
		sY = int(size[1])

		arrayGems = []
		for pos in positions:
			data = pos.split(",")
			column = int(data[0])
			line = int(data[1])
			value = int(data[2])
			arrayGems.append(value)
			matrix[line][column] = str(value)

		global media
		media = sum(arrayGems)/float(len(arrayGems))

		matrix[int(init[0])][int(init[1])] = "0"

		#for row in matrix:
		#	print row


		matrix2 = []


		limit1 = iY-time
		if limit1<=0: limit1=0

		limit2 = iY+time+1
		if limit2>=sY: limit2=sY

		limit3 = iX-time
		if limit3<=0: limit3=0

		limit4 = iX+time+1
		if limit4>=sX: limit4=sX

		#IMPORTANT! if the matrix is bigger than the time available to walk it we have to 
		#truncate to make the algorithm way more efficient. (less data to copy in each iteration)
		for i in range(limit1,limit2):
			matrix2.append(matrix[i][limit3:limit4])

		matrix = matrix2;

		
		sX = len(matrix[1])
		sY = len(matrix)

	
		solveMatrix(matrix,iX,iY,time,[iX,iY],gems)
		print max(superArray)



#Recursive function that explores all posible paths of the game
def solveMatrix(matrix,iX,iY,time,anterior,gems,total=0):
	
	if time==0 or gems==0:
		# If there is no more time or gems, the game is over
		addToArray(total)
		return

	#Get all the new possible paths for the current position.
	lista=expand(iX,iY,anterior)
	newTime = time
	for elem in lista:
		#Each iteration modifies the matrix so we have to make a copy of it
		#The same for the time, gems and other values.
		matrixNew = copy.deepcopy(matrix)
		value = int(matrixNew[elem[0]][elem[1]])
		matrixNew[elem[0]][elem[1]] = "0"
		newGems = copy.deepcopy(gems)

		#We found a gem
		if value!=0: newGems=newGems-1
		newTotal = copy.deepcopy(total)
		newTotal=newTotal+value
		
		#When to stop the search, if the remaining time/gems is not enough to get a good score 
		global superArray
		if (newTotal+3.8*time)<max(superArray):
			continue
	
		if (newTotal+2.5*newGems)<max(superArray):
			continue

		#solve the matrix for every new path
		solveMatrix(matrixNew,elem[0],elem[1],newTime-1,[iX,iY],newGems,newTotal)


#Add score to array
def addToArray(total):
	global superArray
	superArray.append(total)


#For each iteration, expand every possible new path
def expand(x,y,anterior):
	array = []
	#print sX
	if x<sX-1:
		array.append([x+1,y])
	if y<sY-1:
		array.append([x,y+1])
	if x>0:
		array.append([x-1,y])
	if y>0:
		array.append([x,y-1])

	#We can't go back to the previous position
	if anterior in array:
		array.remove(anterior)
	return array




if __name__ == '__main__':
	main()