#pradip_warkhade_292

for i in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split(" ")))
    sum1=1
    flag=0
    for j in range(len(l)):
        sum1=sum1*l[j]
        
        if(sum1%b==0):
            flag=1
        else:
            continue
    if(flag==0):
        print("NO")
    else:
        print("YES")
            
    

        
    
            
        
            
            