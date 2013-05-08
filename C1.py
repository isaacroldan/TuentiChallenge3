
########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 1
#  Isaac Roldán (@saky)
#  
##########################################



#Find Next min
def findMin(array,index):
	if index==0:
		mini = array[index]
		index = index+1

	for j in range(index,len(array)):
		if array[j]<=array[j-1]:
			mini = array[j]
		else:
			return mini, j

	return mini,len(array)

#Find Next Max
def findMax(array,index):

	if index==len(array): return 1,index
	for j in range(index,len(array)):
		if array[j]>=array[j-1]:
			maxi = array[j]
		else:
			return maxi, j

	return maxi,len(array)



def main():
	num=0
	testCases = int(raw_input(""))
	for i in range(testCases):
		try:
			budget = int(str(raw_input("")))
			array = str(raw_input("")).split(" ")
			array = [int(i) for i in array]
		except EOFError:
			break

		k=0	
		#itarate until the end of the array
		#The last operation has to be a multiplication (after finding a Max)
		while(1):
			mini,k = findMin(array,k)
			if k ==len(array): break
			budget=budget/mini

			maxi,k = findMax(array,k)
			budget=budget*maxi
			if k==len(array): break

		print budget

if __name__ == '__main__':
	main()


