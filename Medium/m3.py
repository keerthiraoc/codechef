def combinotrics(c,d):
    if 2*d > c:
        d = c - d
    if d < 0:
        return 0
    bn = 1
    for j in range(c-d+1, c+1):
        bn *= j
    for j in range(2,d+1):
        bn //= j
    return bn
    
for i in range(int(input())):
    k,n=map(int,input().split())
    if n==k:
        print(1)
    else:
        print(combinotrics(k-1,n-1))