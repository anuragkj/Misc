def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

def getProduct(n):
 
    product = 1
 
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
 
    return product    


test_case = int(input())
for t in range(test_case):
    start, end = input().split()
    start = int(start)
    end = int(end)
    count = 0
    for i in range(start, end + 1):
        sumd = getSum(i)
        productd = getProduct(i)
        if productd % sumd == 0:
            count +=1
            
    print("Case #"+str(t+1) + ": "+str(count))