import random

myList = [random.randint(-30, 30) for i in range(30)]



p=0
for x in range(30):
	for y in range(30):
		for z in range(30):
			if (myList[x] + myList[y] + myList[z] == 0 ):
				p= p + 1
				print myList[x] , 	myList[y] , myList[z]																																																	
if p==0: 
	print  "Den uparxei tetoios sundiasmos"