# Mock Project 1 // Autor: @pgdada

from datetime import datetime as dt

allowedUsers = ['Dada', 'Seyi', 'Mike', 'Love']
allowedPasswords = ['passwordDada', 'passwordSeyi', 'passwordMike', 'passwordLove']
acctBalances = [2500, 300205, 50, 13000590.60]

name = input("What is your username? \n")
if name in allowedUsers:
    password = input("Your password? \n")
    userID = allowedUsers.index(name)
    
    if password == allowedPasswords[userID]:
        time = dt.now().strftime("%H:%M")
        date = dt.today().strftime('%m/%d/%y')
        print(f"Today: {date}, Time : {time}")
        print(f'Welcome {name}')
        balance = acctBalances[userID]
        
    else:
        print('Password Incorect, please try again')
else:
    print('Name not found, please try again')

atmTerminal = True
while atmTerminal:
    print('''these are the available options:
    1. Withdrawal
    2. Cash Deposit
    3. Complaint
    0. Exit
    ''')
    selectedOption = int(input('Please select an option: '))
    
    if selectedOption == 1:     #WITHDRAWAL
        withdrawal = float(input("How much would you like to withdraw? \n"))
        balance -=withdrawal
        print("Take your cash!")

    elif selectedOption == 2:   #DEPOSIT
        deposit = float(input("How much would you like to deposit? \n"))
        balance += deposit
        print(f"Your current balance: {balance}")

    elif selectedOption == 3:   #COMPLAINTS
        complaint = input("What issue will you like to report? \n")
        print("Thank you for contacting us.")

    elif selectedOption == 0:
        atmTerminal = False
        print("Have a nice day!")
        break

    else:
        print('Invalid selection, please try again')
        continue

acctBalances[userID] = balance
