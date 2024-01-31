# cook your dish here
try:
    T = int(input())
    even = []
    odd = []
    p=0
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split(" ")))
        for j in A:
            if(j%2!=0):
                odd.append(j)
            else:
                even.append(j)
        if(len(odd)==0):
            p=1
            
        if((len(odd)-1)%2)!=0 and p==0:
            print("YES")
    
        else:
            print("NO")
        
        even = []
        odd = []
        A=[]
        p=0
except:
    pass