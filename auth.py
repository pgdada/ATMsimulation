# Authorization Code in Python
# Author: @pgdada // 04/03/2021

import random
from datetime import datetime as dt
from getpass import getpass
import database as db


# Initialization & Login
def init():
    haveAccount = input(
'''Do you have an account with us?
Enter: 
    Y. Yes
    N. No
    0. Exit

''')
    # haveAccount = int(haveAccount)
    if haveAccount.upper() == 'Y':
        account, userDetails = login()
        return account, userDetails
    elif haveAccount.upper() == 'N':
        success = register()
        if not success:
            account, userDetails = init()
        else:
            account, userDetails = login()
        return account, userDetails
    else:
        try:
            int(haveAccount) == 0
        except Exception:
            print('Please select a valid option\n')
            init()
        else:
            print('Good bye')
            exit()


# Register: username or email & password required
def register():
    firstName = input('\nWhat is your first name? \t')
    lastName = input('What is your last name? \t')
    email = input('\nEnter your email address: \t')
    if db.email_exists(email):
        print("This email already exists in our records, try logging in")
        return False
    else:
        # newPassword = input('\nCreate a new password:\t')
        newPassword = getpass('Create a new password: \t')
        newAccount = accountGen()
        newBalance = 0.00
        newUser = [firstName, lastName, email, newPassword, str(newBalance)]
        db.create(newAccount, newUser)
        print(f'\nWelcome to Divus Bank, your new Account Number is {newAccount} \n')
        return True

def accountGen():
    print('\nGenerating your Account Number............................', flush=True)
    num = random.randrange(1000000001, 9999999999)
    # Making sure there's unique Account Numbers
    if db.account_exists(num):
        accountGen()
    else:
        return num

# Login: username or email & password required
def login():
    print('\n********** Login to your Account **********\n')
    account = int(input('Enter Account Number:\t'))
    # password = input('Enter password:      \t')
    password = getpass('Enter password:      \t')
    
    try:
        userDetails = db.authenticated_user(account, password)
    except Exception:
        print('\nInvalid account or password, try again\n')
        login()
    else:
        time = dt.now().strftime("%H:%M")
        date = dt.today().strftime('%m/%d/%y')
        print(f'\nToday: {date}, Time: {time}')
        print(f'\nWelcome {userDetails[0]},')
        return account, userDetails

def logout():
    print('\nSuccessfully logged out. Have a nice day!\n')
    exit()


# Bank Operations on User details
def bankOperation(account, userDetails):
    print('''
these are the available options:
    1. Withdrawal
    2. Cash Deposit
    3. Complaint
    0. Exit''')
    selectedOption = input('\nPlease select an option:\t')

    try:
        selectedOption = int(selectedOption)
    except Exception:
        print('\nInvalid selection, please try again')
    else:
        if selectedOption == 1:     #WITHDRAWAL
            withdrawalOperation(userDetails)
        elif selectedOption == 2:   #DEPOSIT
            depositOperation(userDetails)
        elif selectedOption == 3:   #COMPLAINTS
            complaintOperation(userDetails)
        elif selectedOption == 0:
            logout()
    finally:
        db.update(account, userDetails)

def withdrawalOperation(userDetails):
    # Casting to float
    userDetails[4] = float(userDetails[4])
    # Transaction
    withdrawAmt = float(input('\nHow much would you like to withdraw?\n\n'))
    if withdrawAmt < userDetails[4]:
        userDetails[4] -=withdrawAmt
        print('\nTake your cash!')
    else:
        print(f'\nYour current balance:\t{userDetails[4]}')
        print('\nEnter a valid amount:\t')
        withdrawalOperation(userDetails)
    # Re-casting to string
    userDetails[4] = str(userDetails[4])

def depositOperation(userDetails):
    # Casting to float
    userDetails[4] = float(userDetails[4])
    # Transaction
    depositAmt = float(input('\nHow much would you like to deposit? \n\n'))
    if depositAmt > 0:
        userDetails[4] += depositAmt
        print(f'\nYour current balance: {userDetails[4]}')
    else:
        print('\nEnter a valid amount:\t')
        depositOperation(userDetails)
    # Re-casting to string
    userDetails[4] = str(userDetails[4])

def complaintOperation(userDetails):
    complaint = input('\nWhat issue will you like to report? \n\n')
    print(f'\n{userDetails[0].title()}, thank you for contacting us.')
