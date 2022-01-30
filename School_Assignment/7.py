dic = {}
print("Welcome to the birthday record!!!")
while(True):
    print("")
    print("Choose one of the following: ")
    print("1: Search a person's birthday")
    print("2: Add record")
    print("3: Change an existing record")
    print("4: Delete a record")
    print("0: Exit")
    print("")
    choice = int(input("Enter your choice: "))
    if(choice == 0):
        break
    elif(choice == 1):
        print("")
        search = input("Enter the name: ")
        if search in dic:
            print("Birthday: "+dic[search])
        else:
            print("Record does not exist")
    elif(choice == 2):
        print("")
        name = input("Enter name: ")
        dob = input("Enter DOB: ")
        dic[name] = dob
    elif(choice == 3):
        print("")
        search = input("Enter the name: ")
        if search in dic:
            dob = input("Enter new DOB: ")
            dic[search] = dob
        else:
            print("Record does not exist")
    elif(choice == 4):
        print("")
        search = input("Enter the name: ")
        if search in dic:
           dic.pop(search, None)
        else:
            print("Record does not exist")
    else:
        print("Invalid choice")
        continue
        