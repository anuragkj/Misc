test_case = int(input())
for t in range(test_case):
    n = int(input())
    old = input()
    upper = 0
    lower = 0
    special = 0
    digit = 0
    new = old
    for i in old:
        if i.isalnum():
            if i.isalpha():
                if i.isupper():
                    upper+=1
                else:
                    lower+=1
            else:
                digit+=1
        else:
            if i in ['#','@','&','*']:
                special+=1
    if upper == 0:
        new += 'A'
    if lower == 0:
        new+= 'a'
    if digit == 0:
        new+= '1'
    if special == 0:
        new+= '@'
    if len(new)<7:
        new += (7 - len(new))*'1'
    print("Case #"+str(t+1) + ": "+str(new))
    
    
