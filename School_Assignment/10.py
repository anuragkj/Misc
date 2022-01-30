#Write a program that accepts a list from user and print the alternate element of list.
val = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    val.append(numbers)
print("Original List is:",val)

print('Alternate elements are:')

for i in range(0,num,2):
    print(val[i])