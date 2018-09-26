def foo(s):
    length=len(s)
    if length<2:
        k=int('0'+s)+1
        if k==10:k=11
        return(str(k))
    m=length//2
    mdc=(s[m] if length%2 ==1 else '')
    rst = list(reversed(n[0:m]))
    en = s[-m:length]
    inc_st =True
    for sc,ec in zip(rst,en):
        if ec < sc:
            inc_st = False
        elif ec > sc:
            break
    
    if inc_st:
        if mdc =='9':
            mdc ='0'
        elif mdc !='':
            mdc = str(1+int(mdc))
            inc_st = False
    
    if inc_st:
        for p,c in enumerate(rst):
            if c!='9':
                rst[p] =str(1+int(c))
                inc_st = False
                break
            else:
                rst[p] ='0'

        if inc_st:
            rst[-1] ='1'
            mdc = mdc+'0'

    return(''.join((*reversed(rst),mdc, *rst)))

for _ in range(int(input())):
    n = str(input())
    print(foo(n))