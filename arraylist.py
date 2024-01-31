# cook your dish here
count=0 
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]>=10):
        count+=1 
print(count)
        