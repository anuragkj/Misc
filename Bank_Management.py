import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    pin = 0
    
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        while(True):
            self.type = input("Enter the type of account [C/S] : ")
            if self.type in ('c','s','C','S'):
                if self.type == 'c' or self.type == 'C':
                    self.type = "Current"
                else:
                    self.type = "Savings"
                break
            else:
                print("Please enter a valid account type") 
        while(True):
            self.deposit = int(input("Enter The Initial amount (>=500 for Saving and >=1000 for current) : "))
            if self.type =="Current":
                if self.deposit >= 1000:
                    break
            elif self.type =="Savings":
                if self.deposit >= 500:
                    break
            print("Please enter valid amount")
        self.pin= int(input("Enter the pin : "))
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name : ")
        self.type = input("Modify type of Account : ")
        self.deposit = int(input("Modify Balance : "))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("**********************")
    print("BANK MANAGEMENT SYSTEM")
    print("**********************")

    print("Created by Shambhavi Jha:")
    input("Press enter to continue...")



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    print("Table is in the format Account number, Account name, Account Type and Account Salary\n")
    file = pathlib.Path("accounts.bin")
    if file.exists ():
        infile = open('accounts.bin','rb')
        mylist = pickle.load(infile)
        dict = {}
        for item in mylist :
            dict["accNo"] = item.accNo
            dict["name"] = item.name
            dict["type"] = item.type
            dict["deposit"] = item.deposit
            print(dict["accNo"]," ", dict["name"], " ",dict["type"], " ",dict["deposit"] )
        infile.close()
    else :
        print("No records to display")
        

def displaySp(num, numpin): 
    file = pathlib.Path("accounts.bin")
    if file.exists ():
        infile = open('accounts.bin','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num: 
                if item.pin == numpin :
                    print("Your account Balance is = ",item.deposit)
                    found = True
                else:
                    print("Account and pin do not match!!")
                    return
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

def depositAndWithdraw(num1,num3, num2): 
    file = pathlib.Path("accounts.bin")
    if file.exists ():
        infile = open('accounts.bin','rb')
        mylist = pickle.load(infile)
        infile.close()
        #os.remove('accounts.bin')
        for item in mylist :
            if item.accNo == num1:
                if item.pin == num3 :
                    if num2 == 1 :
                        amount = int(input("Enter the amount to deposit : "))
                        item.deposit += amount
                        print("Your account is updated")
                    elif num2 == 2 :
                        amount = int(input("Enter the amount to withdraw : "))
                        if amount <= item.deposit :
                            item.deposit -=amount
                        else :
                            print("You cannot withdraw larger amount")
                else:
                    print("Account and pin do not match!!")
                    return
    else :
        print("No records to Search")
        return
    outfile = open('accounts.bin','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    #os.rename('accounts.bin', 'accounts.bin')

    
def deleteAccount(num, numpin):
    file = pathlib.Path("accounts.bin")
    if file.exists ():
        infile = open('accounts.bin','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.pin == numpin:
                if item.accNo != num :
                    newlist.append(item)
            else:
                print("Account and pin do not match")
                return
        #os.remove('accounts.bin')
        outfile = open('accounts.bin','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        #os.rename('accounts.bin', 'accounts.bin')
     
def modifyAccount(num, numpin):
    file = pathlib.Path("accounts.bin")
    if file.exists ():
        infile = open('accounts.bin','rb')
        oldlist = pickle.load(infile)
        infile.close()
        #os.remove('accounts.bin')
        for item in oldlist :
            if item.accNo == num:
                if item.pin == numpin:
                    item.name = input("Enter the account holder name : ")
                    item.type = input("Enter the account Type : ")
                    item.deposit = int(input("Enter the Amount : "))
                else:
                    print("Account and pin do not match")
                    return
        
        outfile = open('accounts.bin','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        #os.rename('accounts.bin', 'accounts.bin')
   

def writeAccountsFile(account) : 


    
    
    file = pathlib.Path("accounts.bin")
    if file.exists ():
        acc_set = []
        infile = open('accounts.bin','rb')
        oldlist = pickle.load(infile)
        for item in oldlist :
            acc_set.append(item.accNo)
        if(account.accNo not in acc_set):
            oldlist.append(account)
            infile.close()
            #os.remove('accounts.bin')
        else:
            print("Account number already exists!!")
            return
    else :
        oldlist = [account]
    outfile = open('accounts.bin','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    #os.rename('accounts.bin', 'accounts.bin')
    print("Account Created")
    
        
# start of the program
ch=''
num=0
intro()

while ch != 8:
    #system("cls");
    print("\n")
    print("MAIN MENU")
    print("1. NEW ACCOUNT")
    print("2. DEPOSIT AMOUNT")
    print("3. WITHDRAW AMOUNT")
    print("4. BALANCE ENQUIRY")
    print("5. ALL ACCOUNT HOLDER LIST")
    print("6. CLOSE AN ACCOUNT")
    print("7. MODIFY AN ACCOUNT")
    print("8. EXIT")
    ch = input("Select Your Option (1-8): ")
    print("\n")
    #system("cls");
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("Enter The account No. : "))
        numpin = int(input("Enter the pin : "))
        depositAndWithdraw(num, numpin , 1)
    elif ch == '3':
        num = int(input("Enter The account No. : "))
        numpin = int(input("Enter the pin : "))
        depositAndWithdraw(num, numpin , 1)
    elif ch == '4':
        num = int(input("Enter The account No. : "))
        numpin = int(input("Enter the pin : "))
        displaySp(num, numpin)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("Enter The account No. : "))
        numpin = int(input("Enter the pin : "))
        deleteAccount(num, numpin)
    elif ch == '7':
        num = int(input("Enter The account No. : "))
        numpin = int(input("Enter the pin : "))
        modifyAccount(num, numpin)
    elif ch == '8':
        print("Thanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    
    #ch = input("Enter your choice : ")