#Find and display the largest number of a lst without using built-in function maxm(). Your program should ask the user to input values in lst from keyboard.
val = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number: '))
    val.append(numbers)
print("Original List is:",val)

maxm = 0
for data in val:
    if data > maxm:
        maxm = data

print('The largest number in lst is', maxm)