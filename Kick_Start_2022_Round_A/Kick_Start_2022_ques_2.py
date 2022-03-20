def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum



test_case = int(input())
for t in range(test_case):
    N = int(input())
    num_sum = getSum(N)
    k = (9 - (num_sum%9))%9
    str_num = str(N)
    ini_len = len(str_num)
    output = ""
    if k < int(str_num[0]):
        output = str(k) + str_num
    else:
        for i in range(1, ini_len):
            if k < int(str_num[i]):
                output = str_num[0:i] + str(k) + str_num[i:]
                break
        if output == "":
            output = str_num+str(k)
    if output[0] == "0":
        output_list = list(output)
        temp = output_list[0]
        output_list[0] = str(output_list[1])
        output_list[1] = str(temp)
        output = ''.join(output_list)
    print("Case #"+str(t+1) + ": "+str((output)))