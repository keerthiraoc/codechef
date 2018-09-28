for _ in range(int(input())):
   n=int(input())
   i=0
   while(n>2048):
       i=i+1
       n=n-2048
   s=bin(n)
   print(i+s.count("1"))