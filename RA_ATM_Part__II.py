import random

database_user = {'Seyi':'passwordSeyi',
    'Mike':'passwordMike',
    'Love':'passwordLove'
}

database = {}

def login():
    #login function here
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name]):
        print("Welcome " + name + "!")
        return True
    
    else:
        print("Password or Username Incorrect. Please try again")
        return False

def register():
    print("***** Register *****")
    
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("Create a password for yourself. \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your account has been created!")
    print(" ... ")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe!")
    print(" == ==== ===== ===== ===")

    login()

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)


def bankOperations():
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option: \n'))
            
    if(selectedOption == 1):
        print('You selected %s' % selectedOption)
        bankOperations()
                
    elif(selectedOption == 2):
        print('You selected %s' % selectedOption)
        bankOperations()
                
    elif(selectedOption == 3):
        print('You selected %s' % selectedOption)
        reportIssue = input("What issue would you like to report? \n")

        print("Thank you for contacting us!")
        bankOperations()

    elif(selectedOption == 4):
        bankOperations()

    else:
        print('Invalid option selected, please try again.')


print("Welcome! What would you like to do?")
print("1. Login")
print("2. Register")

actionSelect = int(input("Select an option \n"))

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()

    bankOperations()

if(actionSelect == 2):
  register()
            
else:
    print('Login failed, username or password incorrect')