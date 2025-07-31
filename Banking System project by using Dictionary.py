print("_____________________________________")
print("           Bank Management System     ")
print("_____________________________________")

data={}
list1= ["Name", "Address", "Phone", "Govt ID", "Account Type", "Amount"]

def take_data():
    acc_num= input("Enter account number : ")

    for item in list1:
        list2.append(input("Enter %s : "%item))

    data[acc_num] = dict(zip(list1,list2))
    print("Account Created")
    print("-------------------------------------------------------")
    return

def other_options():
    ch=int(input("1. Check Balance \n2. Withdraw \n3. Deposit \nEnter choice :"))

    if ch==1:
        print("Available balance :",data[acc_num] ["Amount"])
        print("-----------------------------------------------------------")

    elif ch==2:
        amt=int(input("Enter amount to withdraw :"))
        new_amt=int(data[acc_num]["Amount"]) - amt
        data[acc_num] ["Amount"]= new_amt
        print("-----------------------------------------------------------")
        print("Withdraw Successful")
        print("Available Balance :", data[acc_num]["Amount"])
        print("-----------------------------------------------------------")

    elif ch==3:
        amt=int(input("Enter amount to deposit :"))
        new_amt=int(data[acc_num]["Amount"]) + amt
        data[acc_num] ["Amount"]= new_amt
        print("-----------------------------------------------------------")
        print("Deposit Successful")
        print("Available Balance :", data[acc_num]["Amount"])
        print("-----------------------------------------------------------")

while True:
    list2= [ ]
    ch= int(input("1. New Customer \n2. Existing Customer \n3. Exit \nEnter choice :"))
    if ch==1:
        take_data()
    if ch==2:
        acc_num = input("Enter your account number :")
        if acc_num in data:
            print("Record Found")
            other_options()
        else:
            print("Record not found")
    if ch==3:
        break
        

        
    
