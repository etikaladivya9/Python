name=input('enter your name')
username=input('enter user name')
password=input('enter password')
conformpassword=input('enter your conformpassword')
balance=int(input('enter balance'))

cpassword=''
if password==conformpassword :
    cpassword=password
    print('registration Successful')
else:
    print("enter correct details")

Lusername=input('enter you username')
lPassword=input('password')

print("Login Successful")



if username==Lusername and password==lPassword:
    while True:
      
        print("1.check balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        Choice=int(input("enter your option"))

            
        if Choice == 1:
         print("Available Balance:", balance)

        elif Choice == 2:
          
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Amount Deposited Successfully")
            print("New Balance:", balance)

        elif Choice ==3:
            amount =int(input("enter your amount"))
            if balance>=amount:

                balance-=amount
                print('Avalible bal',balance)
            else:
                print(".....")    

        elif Choice == 4:
            print("Thank you for using our bank")
            break
        else :
            print("enter valid choice")

else:
    print("enter username and password are invalid")        
        
       

        

      





   
