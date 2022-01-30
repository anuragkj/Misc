#Write a python program to input a list of numbers and swap elements at the even location with the elements at the odd location
val = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    val.append(numbers)
print("Original List is:",val)
s=len(val)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    val[i],val[i+1]=val[i+1],val[i]
print("List after swapping :",val)