# Authorization Code in Python
# Author: @pgdada // 04/03/2021

import random

# Database
database = dict()

# Register: username or email & password required
def register():
    firstName = input('What is your first name?\t')
    lastName = input('Last name?\t')
    email = input('Enter your email address:\t')
    # userName = input('Enter a valid username:')
    password = input('Create a new password:\t')
      
    account = accountGen()
    database[account] = [firstName, lastName, email, password, 0.0]
    print(f'Welcome to Divus Bank, your new Account Number is {account} \n')


# Login: username or email & password required

def login():
    #print('Login to your Account:\n')
    #while True:
    account = input('Enter Account Number:\t')
    password = input('Enter password:      \t')

    if database[account][3] == password:
        userDetails = database[account]
    else:
        print('Invalid account or password, try again\n')
        login()



# Bank job
def accountGen():
    print('Generating your Account Number...')
    return random.randrange(10000000001, 9999999999)



def bankOperation():
    # selectedOption = int
    pass
    

# Welcome message
def init():
    #print('Welcome to Divus Bank\n')
    #while True:
    haveAccount = input('Do you have an account with us?')
    haveAccount = int(haveAccount)
    if haveAccount == 1:
        login()

    elif haveAccount == 2:
        register()
        login()

    # elif haveAccount == 0: #EXIT
    #     break
    else:
        print('Please select a valid option\n')
        init()


def withdrawalOperation():
    pass

def depositOperation():
    pass

def logout():
    print('Thankk you!')
    exit()