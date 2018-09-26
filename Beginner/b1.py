T=int(input())
for N in range(T):
	N=int(input())
	
	x=0
	while N>0:
		x=x+(N%10)
		N=N//10

	print(x)