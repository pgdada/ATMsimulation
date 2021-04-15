# Database Code in Python
# Author: @pgdada // 04/14/2021
# Records : text files

import os
from pathlib import Path
records = "user_records/"


# CREATE FUNCTION
def create(account, user):
    
    try:
        f = open(records + str(account) + ".txt", "x")
    except Exception:
        print("Error creating ")
    else:
        f.write(", ".join(user))
    finally:
        f.close()

# READ FUNCTION
def read(account):
    with open(records + str(account) + '.txt') as f:
        account_info = f.readline().split(',')
        account_info = [item.strip() for item in account_info]
        return account_info

# UPDATE FUNCTION
def update(account, user):
    with open(records + str(account) + '.txt',"w") as f:
        f.write(", ".join(user))

# DELETE FUNCTION
def delete(account):
    # find user with account number
    # delete the user record (file)
    
    try:
        os.remove(records + str(account) + ".txt")
    except FileNotFoundError:
        print("User not found")
    else:
        print("Success! Account deleted.")

# DATABASE AUTHORIZATION
def email_exists(email):
    all_users = list(Path(records).glob('*.txt'))
    
    for user in all_users:
        account_info = read(user.stem)
        if email in account_info:
            return True
    return False

def account_exists(account):
    all_users = list(Path(records).glob('*.txt'))
    all_users = [item.stem for item in all_users]
    
    if str(account) in all_users:
        return True
    else:
        return False

def authenticated_user(account, password):
    if account_exists(account):
        user = read(account)
        if password == user[3]:
            return user
    raise Exception