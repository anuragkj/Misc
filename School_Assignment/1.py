#Write a python program to find the largest/smallest number in a list/tuple.
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    lst.append(numbers)
print("Maximum element is: ", max(lst))
print("Minimum element is: ", min(lst))