from random import randint
a=[]
for i in range(1,101):
	a.append(randint(1,100))
print(a)
n=max(a,key=a.count)
print(a.count(n))
print(n)
