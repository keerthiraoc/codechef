for i in range(int(input())):
    count=0
    n=int(input())
    while n:
        if n%10==4 or n==4:
            count+=1
        n=n//10
    print(count)