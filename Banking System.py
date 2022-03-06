class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)
        account_list.append(self.account_no)

    def displayInfo(self):
        print("\n######################\n")
        print("user first name: ", self.first_name)
        print("user last name: ", self.last_name)
        print("user gender: ", self.gender)
        print("user street address: ", self.street_address)
        print("user city: ", self.city)
        print("user email: ", self.email)
        print("user cc number: ", self.cc_number)
        print("user cc type: ", self.cc_type)
        print("user balance: ", self.balance)
        print("user account number: ", self.account_no)

        
def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8][1:]), line[9])


def findUser():
    find_first = input("What is the users first name? ").title()
    find_last = input("What is the users last name? ").title()
    found = False
    for user in userList:
        if find_first == user.first_name and find_last == user.last_name:
            user.displayInfo()
            print("\n######################\n")
            found = True
    if not found:
        print("\nuser not found")

    
def overdrafts():
    count = 0
    overdraft_total = 0
    print("\nusers with overdrafts: ")
    for user in userList:
        if user.balance < 0:
            print(user.first_name, user.last_name)
            count += 1
            overdraft_total += user.balance
    print("\ntotal number of users with overdraft accounts: ", count)
    print("total amount overdraft by the users: $", overdraft_total.__round__(2))

    
def missingEmails():
    count = 0
    print("Users without emails stored on account:")
    for user in userList:
        if not user.email:
            print(user.first_name, user.last_name)
            count += 1
    print("\ntotal number of users without emails stored on account: ", count)


def bankDetails():
    total_users = 0
    balance_total = 0
    highest_balance = [["", 0]]
    lowest_balance = [["", 0]]
    for user in userList:
        name = user.first_name, user.last_name
        total_users += 1
        balance_total += user.balance
        if user.balance < lowest_balance[0][1]:
            lowest_balance = [[name, user.balance]]
        elif user.balance == lowest_balance[0][1]:  # to allow multiple lowest balances
            lowest_balance.append([name, user.balance])
        elif user.balance > highest_balance[0][1]:
            highest_balance = [[name, user.balance]]
        elif user.balance == highest_balance[0][1]:  # to allow multiple highest balances
            highest_balance.append([name, user.balance])
    print("total number of users: ", total_users)
    print("bank total worth: $", balance_total)
    print("\nuser/s with highest balance:")
    list_output(highest_balance)
    print("\nuser/s with lowest balance:")
    list_output(lowest_balance)


def list_output(a_list):
    for s in a_list:
        print(*s[0], sep=" ")
        print("$", s[1])


def int_check(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("Whoops, entry must be an integer...")


def transfer():
    account_num = input("Please enter an account number: ")
    for user in userList:
        if account_num == user.account_no:
            print("user name: ", user.first_name, user.last_name)
            print("account balance: $", user.balance)
            transfer_amount = int(input("How much money would you like to transfer? "))
            if transfer_amount > user.balance:
                print("\ncannot proceed with transfer. User needs more money.")
            elif transfer_amount >= user.balance:
                transfer_account = int(input("What account would you like to transfer money to? "))

                for user1 in userList:
                    if user1.account_no == transfer_account:
                        confirm = input(f"Is user sure they want to transfer"
                                        f" ${transfer_amount} to {user1.first_name, user1.last_name}?"
                                        f"Press <enter> to continue with transaction, or any other key "
                                        f"and <enter> to return to main menu.\n")
                        if not confirm:
                            return



userList = []
account_list = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()
    
    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()      
    print()

findUser()
