# cook your dish here

for i in range(int(input())):
    x,y=map(int,input().split())
    if(x==y):
        print(x)
    else:
        flag=0
        for i in range(x,y):
            m=i-x
            n=y-i
            if(m!=n):
                continue
            elif(m==n):
                print(i)
                flag=1
        if(flag==0):
            print(-1)

                
            
            
        
    
    