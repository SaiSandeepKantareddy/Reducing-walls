def walls():
	x=int(input("Enter the test cases:"))
	for f in range(x):
		y=list(map(int,input("ENter the walls and utmost height:").split(',')))
		z=list(map(int,input("ENter the walls height:").split(',')))
		for i in z:
			if i<=y[1]:
				continue
			else:
				g=i-y[1]
				v.append(g)
		print(len(v))
		for g in range(len(v)):
			v.pop()
      
 if __name__=='__main__':
    v=[]
    walls()
