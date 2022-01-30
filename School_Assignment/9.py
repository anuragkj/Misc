#Write a program that accepts a list from user. Your program should reverse the content of list and display it. Do not use reverse() method.
val = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    val.append(numbers)
print("Original List is:",val)

L = len(val)

for i in range(int(L / 2)):
    n = val[i]
    val[i] = val[L - i - 1]
    val[L - i - 1] = n
    
print("Final List is:",val)