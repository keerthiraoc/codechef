A=input()
if A == "".join(list(reversed(A))):
	print('pallindrome')
else:
	print('not a pallindrome')

# flag=0
# for i,j in zip(A[::-1],A):
# 	if i !== j:
#         flag = 1
#         break

# if flag == 1:
#     print('not a pallindrome')
# else:
#     print('pallindrome')
