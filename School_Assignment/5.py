#Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have scored marks above 75.
n=int(int(input("Enter number of students: "))) 
d={} 
for i in range(n): 
    print("")
    print("Student number: " + str(i+1))
    roll_no=int(input("Enter roll no: ")) 
    name=input("Enter name: ") 
    marks=int(input("Enter marks: ")) 
    d[roll_no]=[name,marks] 
print("")
print("Students with marks greater than 75: ")
for k in d: 
    if(d[k][1]>75): 
        print(d[k][0]) 