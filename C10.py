########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 10
#  Isaac Roldán (@saky)
#  
##########################################

#The objective is to calc the md5 of some big strings.
# The strings are defined withs sums and multiplications of letters
# This is easy in python, we don't need to "create" the whole strings


# This solution is "fast" but not very efficent in RAM terms.
# It could need even more than 16GB of RAM (no problem in my 16GB Mac with swap)



import re
import hashlib

def main():

	while(1):
		try:
			data = str(raw_input(""))
			calculate(data)
		except EOFError:
			break


def calculate(data):
	data = data.replace("[","*(")
	data = data.replace("]",")")
	finded = re.findall("[a-z][0-9]+", data)
	for item in finded:
		data = data.replace(item,item[0]+"+"+item[1:])
		data = data.replace("++","+")


	data = re.sub(r'(\))([a-z0-9])',r'\1+\2',data)
	data = re.sub("(?P<id>[a-z]+)","\"\g<id>\"",data)
	data = data.replace(")+)","))")

	#Create a string with "+" and "*" replacing the "[" and "]"
	# The final string is something like this:
		#"e"+10*("as"+51*("fg"+20*("dsafg")+"s"+65*("asdf"+12*(34*("sadf")+"asd"+21*("ash")+"jy")+87*("ghg"+92*("sad")+"tr"))+"sdfg")+"jyu"+73*("asdf"))+"f"


	m = hashlib.md5()
	m.update(eval(data))
	res = m.hexdigest()
	print res
	


if __name__ == '__main__':
	main()