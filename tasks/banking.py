customers = [
    {"username": "admin", "password": "1234", "balance": 1000},
    {"username": "user1", "password": "1111", "balance": 2000},
    {"username": "user2", "password": "2222", "balance": 3000}
]

# username = "admin"
# password = "1234"

# balance = 1000


user = input("Enter username: ")
pwd = input("Enter password: ")
# print("Entered:", user, pwd)  # debug

current = None

for  i in customers:  
    if user == i["username"] and pwd ==i["password"]:
        current=i
        bal=current["balance"]
        break
if current:
  print("Login Successful")
        
        
  while True: 
      print("Banking Menu")
      print("1. Deposit")
      print("2. Check Balance")
      print("3. Withdrawl")
      print("4. Exit")        

       
      choice = int(input("Enter your choice: "))

      if choice == 1:
             amount = int(input("Enter amount to deposit: "))
            #  current["balance"]+=amount
             current.update({"balance": current["balance"] + amount})
             print("Amount Deposited Successfully"),
             print("new balance:", current["balance"])
                    

      elif choice == 2:
          print("Available Balance:",current["balance"])

      elif choice == 3:
             amount = int(input("Enter amount to withdrawl:"))
             current["balance"]-=amount
             current.update({"balance": current["balance"] -amount})
             print("Available Balance:",current["balance"])
         
      elif choice==4:
            print("Thank you for using our Bank")
            break
        

      else:
          print("Invalid choice")

else:
    print("Invalid Username or Password")