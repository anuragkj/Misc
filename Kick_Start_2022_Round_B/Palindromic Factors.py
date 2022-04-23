from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


test_case = int(input())
for t in range(test_case):
    num = int(input())
    arr = factors(num)
    total = 0
    for i in arr:
        if str(i) == str(i)[::-1]:
            total += 1
        
    print("Case #"+str(t+1) + ": "+str(total))