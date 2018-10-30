for i in range(int(input())):
    n=int(input())
    b=list(map(int, input().split()))
    a=[]
    for i in range(1,n+1):
        a.append(i)
    for i in range(len(a)):
        if b[i]!=0:
            a.insert((a.index(a[i])-b[i]),a[i])
            a.pop(a.index(a[i])+1)
    print(a)