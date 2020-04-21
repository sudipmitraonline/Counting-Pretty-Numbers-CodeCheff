#@Author : Sudip Mitra
l=['2','3','9']
for x in range(int(input())):
    a,b=map(int,input().split())
    c=0
    for y in range(a,b+1):
        if str(y)[-1] in l:
            c+=1
    print(c)
