#Write a program that keeps student&#39;s name and his marks in a dictionary as key-value pairs. The program should store records of 10 students and display students name and marks of five students in decreasing order of marks obtained.
n=int(int(input("Enter number of students: "))) 
d={} 
for i in range(n): 
    print("")
    print("Student number: " + str(i+1))
    name=input("Enter name: ") 
    marks=int(input("Enter marks: ")) 
    d[name]=marks 

d_sort = sorted(d.items(), key=lambda x: x[1], reverse=True)
k = 0
print("")
print("Top 5 students: ")
for i in d_sort:
	print(i[0], i[1])
	k+=1
	if(k == 5):
	    break