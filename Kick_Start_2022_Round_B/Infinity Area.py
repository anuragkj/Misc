import math
test_case = int(input())
for t in range(test_case):
    r, a, b = input().split()
    r = int(r)
    a = int(a)
    b = int(b)
    total_area = 0
    radius_n = r
    k = 0
    while( int(radius_n) != 0):
        total_area += math.pi * radius_n ** 2
        if(k % 2 == 0):
            radius_n = int(radius_n*a)
        else:
            radius_n = int(radius_n/b)
        k += 1
        
    print("Case #"+str(t+1) + ": "+str(round(total_area,6)))
    
    
