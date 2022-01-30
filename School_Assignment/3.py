#Write a python program to input a list/tuple of elements, search for a given element in the list/tuple
val = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    val.append(numbers)
print("Original List is:",val)
search = int(input("Input number to search: "))
if search in val:
    print("Present in list")
else:
    print("Not present in list")