# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    a=2**y
    b=a//2
    c=a-b
    if(x==1):
        print(c)
    else:
        for i in range(1,x):
            z=c//2
            c=z 
        print(c)
