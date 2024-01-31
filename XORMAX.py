T = int(input())
for tc in range(T):
    # Read string a and b.
    a = input()
    b = input()
	
    if len(a) > len(b):
        b = '0'*(len(a)-len(b)) + b
    elif len(a) < len(b):
        a = '0'*(len(b)-len(a)) + a
    
    a0 = a.count('0')
    a1 = a.count('1')
    b0 = b.count('0')
    b1 = b.count('1')
    
    #print(a0,a1,b0,b1)
    
    for i in range(len(a)):
        # Take 1 from a, Take 0 from b or Take 0 from a, Take 1 from b
        if (a1 > 0 and b0 > 0):
            a1 -= 1 
            b0 -= 1
            print('1', end='')
        elif (a0 > 0 and b1 > 0):
            a0 -= 1 
            b1 -= 1
            print('1', end='')
        elif (a0 > 0 and b0 > 0):
            a0 -= 1 
            b0 -= 1
            print('0', end='')
        elif (a1 > 0 and b1 > 0):
            a1 -= 1 
            b1 -= 1
            print('0', end='')
        else:
            pass
    print('')  
	