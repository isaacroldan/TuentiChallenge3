########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 13
#  Isaac Roldán (@saky)
#  
##########################################

#INFO: We have a big array of "pseudorandom" numbers sorted
#Objective: find the maximum repetitions in a given subarray of that big array.

#Not very efficient in time, but it works and the code is easy.
#Use collections to count the repetitions in the subarray

import re
import hashlib
import collections

def main():
	testCases = int(raw_input(""))
	for case in range(testCases):
		preInfo = raw_input("").split(" ")
		data = raw_input("").split(" ")
		print "Test case #"+str(case+1)
		for o in range(int(preInfo[1])):
			i = raw_input("").split()
			subList = data[int(i[0])-1:int(i[1])]

			suma = [int(y) for x, y in collections.Counter(subList).items()]
			print max(suma)

if __name__ == '__main__':
	main()