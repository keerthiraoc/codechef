t = int(input())
while t:
    n = int(input())
    numbers = list(map(int,input().split()))
    ans = 2000000000
    numbers.sort()
    for i in range(n-1):
        if(ans>numbers[i+1]-numbers[i]):
            ans = numbers[i+1]-numbers[i]  
    print(ans)
    t = t-1