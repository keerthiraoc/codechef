# for _ in range(int(input())):
#     l=[]
#     for i in range(int(input())):
#         l.append(list(map(int,input().split())))
#     for i in range(len(l)-2,-1,-1):
#         for j in range(i+1):
#             l[i][j] += max(l[i+1][j], l[i+1][j+1])
#     print(l[0][0])

# for _ in range(int(input())):
# 	min, max=map(int,input().split())
# 	if min>max:
# 		print(min, min+max)
# 	else:
# 		print(max, min+max)

for _ in range(int(input())):
	a=list(map(int,input().split()))
	a.sort()
	print(a[1])