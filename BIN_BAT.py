# cook your dish here
sum1=0
for i in range(int(input())):
    x,y,z=map(int,input().split())
    c=0
    while(x>0):
        x=x//2
        c=c+1
    print(((c-1)*y)+((c-2)*z))        

         
    
    
    
    
    