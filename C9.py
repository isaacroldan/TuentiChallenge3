########################################## 
#   
#  #TuentiChallenge3 (2013).
#  Challenge 9
#  Isaac Roldán (@saky)
#  
##########################################

# "space invaders"-like game. We have soldiers(1kill/s) and crematories(kills everything just once)
# The "aliens" get at (w/s speed). How much time can we survive?

#After studiying the game, the best solution is always one of these: 
# Buy only soldiers or Buy only Crematories
# The solution can be calculated with some simple formulas, no need to iterate anything


def main():
	testCases = int(raw_input(""))
	for case in range(testCases):
		data = raw_input("").split(" ")
		w = int(data[0])
		h = int(data[1])
		sCost = int(data[2])
		cCost = int(data[3])
		gold = int(data[4])

		maxCrema = gold/cCost


		if gold/sCost>=w:
			print -1
			continue

		numSoldiers = 0
		numCrema = 0
		goldBank = gold
		maxLiveTime = 0



		liveTime = []

		#CASO SOLO SOLDADOS
		numCrema=0
		numSoldiers = gold/sCost
		goldBank = gold - numSoldiers*sCost
		if goldBank>cCost:
			numCrema=goldBank/cCost

		if numCrema==0:
			liveTime.append(((w*h)-w)/(w-numSoldiers)+1)
		else:
			tiempo = ((w*h)-w)/(w-numSoldiers)+1
			liveTime.append(tiempo*(numCrema+1))




		#CASO SOLO CREMATORIOS
		numSoldiers=0
		numCrema=gold/cCost
		goldBank = gold - numCrema*cCost
		if goldBank>sCost:
			numSoldiers=goldBank/sCost

		if numSoldiers==0:
			liveTime.append(h*(maxCrema+1))
		else:
			tiempo = ((w*h)-w)/(w-numSoldiers)+1
			liveTime.append(tiempo*(numCrema+1))




		maxLiveTime = max(liveTime)


		print maxLiveTime


######
#EXTRA: Additional code for iterative searching of best solution
######


# def calcTime(w,h,numSoldiers,numCrema):

# 	array = [0,w] #longitud y numero en el ultimo punto
# 	seconds = 0
# 	debug=0
	
# 	while(1):
# 		seconds+=1
# 		#array.insert(0,10)
# 		array[0]+=1
		
# 		bullets = numSoldiers
# 		if debug: print "t="+str(seconds)," ","len=",array[0]," ",array
# 		if array[0]==h+1: break


# 		for i in range(array[0]-1,-1,-1):
# 			res = array[1]-bullets
# 			if res>=0:
# 				bullets=0
# 				array[1]=res
# 				if array[1]==0:
# 					array[1]=w
# 					array[0]-=1
# 			else:
# 				bullets = bullets-array[1]
# 				array[1]=w
# 				array[0]-=1

# 			if bullets == 0: break

# 		if debug==1: print "t="+str(seconds)," ","len=",array[0]," ",array

# 		if array[0]==h:
# 			if debug: 
# 				print "ALERT!"
# 				print "Tenemos "+str(array[-1])+" Enemigos y solo "+str(numSoldiers)+" balas"
# 				print str(numCrema)+" Crematorios disponibles!"
			
# 			if numCrema>0:
# 				if debug: print "Soldiers insuficientes, inicia Crematorio"
# 				array = [0,w]
# 				numCrema=numCrema-1
# 				continue
# 			else:
# 				if debug:  print "No quedan crematorios!!!"


		

# 	return seconds-1





if __name__ == '__main__':
	main()