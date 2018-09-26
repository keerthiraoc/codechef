W=0
L=0
A=0
B=0
for i in range(int(input())):
    x,y = map(int, input().split())
    A+=x
    B+=y
    if A>B and A-B>L:
        L=A-B
        W=1
    elif A<B and B-A>L:
        L=B-A
        W=2
print(W,L)