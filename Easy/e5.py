t = int(input())
while t:
    n, m = map(int, input().split())
    numbers = list(map(int,input().split()))
    number=[]
    chef=[]
    asst=[]
    for i in range(n):
        number.append(i+1)
    for j in numbers:
        number.remove(j)
    number.sort()
    for i in range(0,len(number),2):
        chef.append(number[i])
        if(i+1)<len(number):
            asst.append(number[i+1])
        elif (i+1) == len(number):
            break
    for i in chef:
        print(i,end=' ')
    print('')
    for i in asst:
        print(i,end=' ')
    t = t-1

    