n,k = map(int,input().split())
tweets=[-1]*n
for x in range(k):
	click = input().split()
	if len(click)>1:
		tweets[int(click[-1])-1]*=-1
	else: tweets =[-1]*n
	print(tweets.count(1))