#pradip_warkhade_292
for i in range(int(input())):
    a,b,c=map(int,input().split())
    x=abs(a-b)
    f=x//c
    r=x%c 
    if(a==b):
        print(0)
    else:
        if(x>c):
            if(r==0):
                print(f+r)
            else:
                print(f+1)
        else:
            print(1)
    
            
        
        
        
            
        
            
            