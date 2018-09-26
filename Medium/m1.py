coins = {0:0,1:1}
def recurse(n):
    if n not in coins:
        n_2 = recurse(n//2)
        n_3 = recurse(n//3)
        n_4 = recurse(n//4)
        coins[n] = max(n,n_2+n_3+n_4)
    return coins[n]

while True:
    try:print(recurse(int(input())))
    except:break