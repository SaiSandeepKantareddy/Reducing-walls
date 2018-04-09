t=int(input())
for f in range(t):
	y,h=map(int,input().split())
	z=list(map(int,input().split()))
	k=0
	for i in z:
		   t=i
		   if(t%h==0):
		       k+=t//h-1
		   else:
		       k+=t//h
	print(k)
