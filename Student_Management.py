import csv11
import pandas as pd
import os
from os.path import exists



def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit(Saves all the work)")


# In[3]:


def add_student():
    global student_fields
    global student_database
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    #print(type(student_database['id'][0]))
    
    student_data = []
    for field in student_fields:
        if(field == 'id' or field == 'roll' or field == 'age'):
            value = int(input("Enter " + field + "(Integer value): "))
            student_data.append(value)
        else:
            value = (input("Enter " + field + ": "))
            student_data.append(value)
    id_list = list(student_database['id'])
    if int(student_data[0]) in id_list:
        print("Student ID already present in database! Please add unique ID")
        return
    else:
        choice = input("\nPress y to confirm entry[y/n]: ")
        if(choice == 'y'):
            student_database.loc[len(student_database)] = student_data
            student_database.to_csv('students.csv', index = False)
            print("Data saved successfully")
            return
        elif(choice == 'n'):
            print("Data not saved")
            return        


# In[4]:


def view_students():
    global student_fields
    global student_database

    print("\n\n--- Student Records ---\n\n")
    print(student_database.to_string(index=False))
    input("Press any key to continue: ")


# In[5]:


def search_student():
    global student_fields
    global student_database
    

    print("--- Search Students ---")
    print("Select the criteria for search: ")
    print("1. Search by ID")
    print("3. Search by Roll")
    print("3. Search by Name")
    print("4. Search by Age")
    print("5. Search by Email")
    print("6. Search by Phone")
    choice = int(input("Enter your choice:"))
    if(choice == 1):
        search_inp = int(input("Enter the ID: "))
        search_df = student_database[student_database['id'] == search_inp]
        if(search_df.shape[0] != 0):
            print("--- Results ---")
            print("ID: "+ str(search_df['id'][0]))
            print("Roll: "+ str(search_df['roll'][0]))
            print("Name: "+ str(search_df['name'][0]))
            print("Age: "+ str(search_df['age'][0]))
            print("Email: "+ str(search_df['email'][0]))
            print("Phone: "+str(search_df['phone'][0]))
        else:
            print("ID No. not found in our database")
          
    elif(choice == 2):
        search_inp = int(input("Enter the roll: "))
        search_df = student_database[student_database['roll'] == search_inp]
        if(search_df.shape[0] != 0):
            print("--- Results ---")
            print(search_df.to_string(index=False))
        else:
            print("Roll No. not found in our database")
          
    elif(choice == 3):
        search_inp = input("Enter the name: ")
        search_df = student_database[student_database['name'] == search_inp]
        if(search_df.shape[0] != 0):
            print("--- Results ---")
            print(search_df.to_string(index=False))
        else:
            print("Name not found in our database")
          
    elif(choice == 4):
        search_inp = int(input("Enter the age: "))
        search_df = student_database[student_database['age'] == search_inp]
        if(search_df.shape[0] != 0):
            print("--- Results ---")
            print(search_df.to_string(index=False))
        else:
            print("Age not found in our database")
          
    elif(choice == 5):
        search_inp = input("Enter the email: ")
        search_df = student_database[student_database['email'] == search_inp]
        if(search_df.shape[0] != 0):
            print("--- Results ---")
            print(search_df.to_string(index=False))
        else:
            print("E-Mail not found in our database")
          
    elif(choice == 6):
        search_inp = input("Enter the phone number: ")
        search_df = student_database[student_database['phone'] == search_inp]
        if(search_df.shape[0] != 0):
            print("--- Results ---")
            print(search_df.to_string(index=False))
        else:
            print("Phone not found in our database")
          
    input("Press any key to continue: ")


# In[6]:


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    c_id = int(input("Enter ID of student to update: "))

    student_data = [0]
    for field in student_fields:
        if(field == 'id'):
            pass
        elif(field == 'roll' or field == 'age'):
            value = int(input("Enter " + field + "(Integer values): "))
            student_data.append(value)
        else:
            value = (input("Enter " + field + ": "))
            student_data.append(value)
    id_list = list(student_database['id'])
    if c_id in id_list:
        choice = input("\nPress y to confirm entry[y/n]: ")
        if(choice == 'y'):
            for p in range(1, len(student_fields)):
                student_database.loc[student_database['id'] == c_id, student_fields[p]] = student_data[p]
            
            
            student_database.to_csv('students.csv', index = False)
            print("Data updated successfully")
            return
        elif(choice == 'n'):
            print("Data not updated")
            return
    else:
        print("Provided ID does not exist")

    input("Press any key to continue: ")


def delete_student():
    global student_fields
    global student_database
    

    print("--- Delete Student ---")
    d_id = int(input("Enter ID to delete: "))
    id_list = list(student_database['id'])
    if d_id in id_list:
        indexNames = student_database[ student_database['id'] == d_id ].index
        student_database.drop(indexNames , inplace=True)
        student_database.to_csv('students.csv', index = False)
        print("Data removed successfully")
    else:
        print("Student ID does not exist")

    

    input("Press any key to continue: ")


# In[ ]:


student_fields = ['id', 'roll', 'name', 'age', 'email', 'phone']

if(os.path.exists('students.csv')):   #If student.csv already exists we read it to our dataframe, else we create a dataframe
    student_database = pd.read_csv('students.csv', dtype = str)
    student_database = student_database.astype(dtype= {"id":"int64",
        "roll":"int64","name":"str","age":"int64","email":"str","phone":"str"})
else:
    student_database = pd.DataFrame(columns = student_fields)


while True:
    display_menu()
    
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

student_database.to_csv('students.csv', index = False)
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")





