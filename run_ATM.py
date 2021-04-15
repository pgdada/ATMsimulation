# Mock Project 1 // Autor: @pgdada

from auth import *

print('\n**************** DIVUS BANK ****************\n')
    
# Initialization, Login of Customer
account, userDetails = init()

# After Login, Bank Operations
atmTerminal = True
while atmTerminal:
    bankOperation(account, userDetails)
