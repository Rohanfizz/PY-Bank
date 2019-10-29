#Bank with functions
'''
author >> RohanSharma
'''

# Globals-
o= 0
accounts = {}

# -----------------------------------------------------------------------------------------------------------------------
class bank():
    def __init__(self,amount):
        self.amount=amount
        
    def deposit(self,d):
        self.amount =  self.amount+d
        print(f'Thanks, your new balance is {self.amount} and {d} has been deposited.')
        
    def withdraw(self,w):
        if w>self.amount:
            print('Sorry you are OUT OF BONDS!')
        else:
            self.amount = self.amount - w
            print(f'Thanks, your new balance is {self.amount} and {w} has been withdrawn')

#-----------------------------------------------------------------------------------------------------------------------

def welcome():
    global o
    print('Welcome to ROHAN STATE BANK.')
    print('How may we help you?\n1 = New Account\n2 = Deposite\n3 = Withdraw\n4 = Check balance\n5 = Exit Bank')
    while True:
        try:
            o = int(input('Please enter the option: '))
            break
            
        except ValueError:
            o = print('Option can only be a number between 1 to 5.\n')
    print(' \n ' )
#-----------------------------------------------------------------------------------------------------------------------

def newacc():
    global accounts
    while True:
        name = str.upper(input("Please enter the account holders name: "))
        if name == '':
            print('Please Enter something')
        else:
            break
    while True:
        try:
            amount = int(input("Please enter the starting balance: "))
            if amount >= 5000:
                break
            else:
                print('Starting amount should be more than 5000\n')
        except ValueError:
            print('Amount can only be a number')
    accounts.update( {name: amount} )
    print('New account in the name of {} and with initial balance {} is succesfully made!\n'.format(name,accounts[name]))
    print(accounts)
#-----------------------------------------------------------------------------------------------------------------------
def depo():
    global accounts
    a = str.upper(input('Please enter account holder\'s name: '))
    for i in accounts:
        if a == i:
            while True:
                try:
                    ad= int(input('Please enter the amount you want to Deposit: '))
                    break
                except ValueError:
                    print('Please Enter only a Number')
            accounts[a]+= ad
            print('\nAmount of {} is deposited\nYour new balance is Rs. {}'.format(ad,accounts[a]))
            print(' \n ' )
            break
        
    else:
        print('Sorry, No account found!\n')
        print(' \n ' )
#-----------------------------------------------------------------------------------------------------------------------
def withd():
    global accounts
    b = str.upper(input('Please enter account holder\'s name: '))
    for i in accounts:
        if b == i:
            sb= int(input('Please enter the amount you want to Withdraw: '))
            if sb<= accounts[b]:
                accounts[b]-=sb
                print('\nAmount of {} is deposited\nYour new balance is Rs. {}'.format(sb,accounts[b]))
                print(' \n ' )
                break
            else:
                print("Sorry, you are OUT OF BONDS!")
                break 
            
    else:
        print('Sorry, No account found!\n')
        print(' \n ' )
        
#-----------------------------------------------------------------------------------------------------------------------
def chq():
    global accounts
    
    chker = str.upper(input('Enter The Account holder name: '))
    for q in accounts:
        if q == chker:
            print('Your current balance is: {}\n'.format(accounts[q]))
            break
        else:
            continue
    else:
        print('Sorry no account of name {} was found\n'.format(chker))
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def play():
    global o
    global accounts
    while True:
        welcome()
        if o == 1:
            newacc()
        elif o == 2:
            depo()
        elif o == 3:
            withd()
        elif o ==4:
            chq()
        
        elif o==5:
            print('Thanks for visiting our bank, Do come again!\n')
            break
        else:
            print('Option can only be a number between 1 to 5\n')

if __name__ == '__main__':
    play()