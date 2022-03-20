test_case = int(input())
for t in range(test_case):
    I = input()
    P = input()
    I_marker = 0
    for o in P:
        if o == I[I_marker]:
            I_marker += 1
            if I_marker == len(I):
                break
    if I_marker == len(I):
        print("Case #"+str(t+1) + ": "+str(len(P) - len(I)))
    else:
        print("Case #"+str(t+1) + ": "+"IMPOSSIBLE")