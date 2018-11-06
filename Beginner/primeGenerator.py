def prime(n):
	if n==0 or n==1:
		return 1
	else:
		flag = 0
		for i in range(2,n):
			if n%i == 0:
				flag = 1
		if flag == 0:
			return 1
		else:
			return 0

for i in range(int(input())):
	if prime(i):
		print(i)