# Mock Project 1 // Autor: @pgdada

import random
from datetime import datetime as dt

database = {
    1972856286: ['Johannes', 'Cincinnatus', 'jc-main@gmail.com', 'JCpassword', 168764.55], 
    9025766407: ['Rachel', 'Green', 'rgreen@yahoo.com', 'RGpassword', 135.0], 
    8557279574: ['Ross', 'Geller', 'profgeller@nyu.edu', 'RGpassword', 12389.0], 
    6748795907: ['Monica', 'Geller', 'coolmonica@gmail.com', 'MGpassword', 5630.0], 
    5762680415: ['Chandler', 'Bing', 'cbing@gmail.com', 'CBpassword', 35020.0], 
    6920234738: ['Joey', 'Tribbiani', 'joe69hyd@ymail.com', 'JTpassword', 1309.88], 
    5139963051: ['Phoebe', 'Buffay', 'pheebs51@aol.com', 'PBpassword', 987.92]
    }


def main():
    print('\n**************** DIVUS BANK ****************\n')
    
    # Initialization, Login of Customer
    userDetails = init()

    # After Login, Bank Operations
    atmTerminal = True
    while atmTerminal:
        bankOperation(userDetails)



# ALL FUNCTIONS

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
        userDetails = login()
        return userDetails

    elif haveAccount.upper() == 'N':
        register()
        userDetails = login()
        return userDetails

    elif int(haveAccount) == 0: #EXIT
        print('Good bye')
        exit()

    else:
        print('Please select a valid option\n')
        init()


# Register: username or email & password required
def register():
    firstName = input('\nWhat is your first name?\t')
    lastName = input('What is your last name?\t')
    email = input('\nEnter your email address:\t')
    newPassword = input('\nCreate a new password:\t')
    newAccount = accountGen()
    newBalance = 0.00
    database[newAccount] = [firstName, lastName, email, newPassword, newBalance]
    print(f'\nWelcome to Divus Bank, your new Account Number is {newAccount} \n')

def accountGen():
    print('\nGenerating your Account Number...', flush=True)
    temp = random.randrange(1000000001, 9999999999)
    # Making sure there's unique Account Numbers
    if temp not in database.keys():
        return temp
    else:
        accountGen()

# Login: username or email & password required
def login():
    print('\n********** Login to your Account **********\n')
    account = int(input('Enter Account Number:\t'))
    password = input('Enter password:      \t')

    if account in database.keys():
        if database[account][3] == password:
            userDetails = database[account]
            time = dt.now().strftime("%H:%M")
            date = dt.today().strftime('%m/%d/%y')
            print(f'\nToday: {date}, Time: {time}')
            print(f'\nWelcome {userDetails[0]},')
            return userDetails

    else:
        print('\nInvalid account or password, try again\n')
        login()

def logout():
    print('\nHave a nice day!\n')
    exit()


# Bank Operations on User details
def bankOperation(userDetails):
    print('''
these are the available options:
    1. Withdrawal
    2. Cash Deposit
    3. Complaint
    0. Exit''')
    selectedOption = int(input('\nPlease select an option:\t'))
    
    if selectedOption == 1:     #WITHDRAWAL
        withdrawalOperation(userDetails)

    elif selectedOption == 2:   #DEPOSIT
        depositOperation(userDetails)

    elif selectedOption == 3:   #COMPLAINTS
        complaintOperation(userDetails)

    elif selectedOption == 0:
        logout()

    else:
        print('\nInvalid selection, please try again')
        bankOperation(userDetails)


def withdrawalOperation(userDetails):
    withdrawAmt = float(input('\nHow much would you like to withdraw?\n\n'))
    if withdrawAmt < userDetails[4]: # balance:
        userDetails[4] -=withdrawAmt
        print('\nTake your cash!')
    else:
        print(f'\nYour current balance:\t{userDetails[4]}')
        print('\nEnter a valid amount:\t')
        withdrawalOperation(userDetails)

def depositOperation(userDetails):
    depositAmt = float(input('\nHow much would you like to deposit? \n\n'))
    if depositAmt > 0:
        userDetails[4] += depositAmt
        print(f'\nYour current balance: {userDetails[4]}')
        print(userDetails)
        print(database)
    else:
        print('\nEnter a valid amount:\t')
        depositOperation(userDetails)

def complaintOperation(userDetails):
    complaint = input('\nWhat issue will you like to report? \n\n')
    print(f'\n{userDetails[0].title()}, thank you for contacting us.')


if __name__ == '__main__':
    main()