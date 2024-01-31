#pradip_warkhade_292
for i in range(int(input())):
    a=int(input())
    l1=list(map(int,input().split(" ")))
    l1.sort()
    start=1
    summ=0
    flag=0
    for p in range(len(l1)):
        if(l1[p]>start):
            flag=1 
            break
        elif(start==l1[p]):
            summ+=0
        else:
            summ+=start-l1[p]
        start+=1
        
    if(flag==0):
        print(summ)
    else:
        print("-1")
            
        
            
            