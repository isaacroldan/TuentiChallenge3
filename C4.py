########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 4
#  Isaac Roldán (@saky)
#  
##########################################

#Info: Find the lost numbers in a big file of integers.
#There are 100 lost integers in the range 1-(2^31-1)

#IMPORTANT: after reviewing the file, the lost numbers are in the first and last part of the file
# so we ignore the rest of it.

import struct
from bitstring import BitArray
import random
import os
import struct
import numpy
import ctypes
import sys

def main():
	testCases = int(raw_input(""))
	result = findLost("integers")
	for i in range(testCases):
		number = int(raw_input(""))
		print result[number-1]

		
def findLost(filename,bytes=4,endian='<I'):
	buf_size=400000 #Buffer enough to catch the first part where the lost numbers are
	buf=ctypes.create_string_buffer(buf_size)
	new_buf=[]
	with open(filename,'rb') as f:
		new_buf = []
		st=f.read(buf_size)
		l=len(st)
		fmt=endian[0]+str(l/bytes)+endian[1]    
		new_buf.extend(struct.unpack_from(fmt,st))

		f.seek(-buf_size,2) #seek to the last part of the file
		st=f.read(buf_size)
		l=len(st)
		fmt=endian[0]+str(l/bytes)+endian[1]    
		new_buf.extend(struct.unpack_from(fmt,st))
	     
	#lost numbers are between [1,100000] and [2^31-100000,2^31-1]
	new_buf.sort()  
	anterior = 0
	array=[]
	for item in new_buf:
		dif = abs(item-anterior)
		if dif>100000:
			anterior = item
			continue
		if dif>1:
			array.append(item-1)

		anterior = item

	return array




	
if __name__ == '__main__':
	main()