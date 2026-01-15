# Function to check and display current balance
def get_balance():
    # Open balance file in read mode
    with open("balance.txt", "r") as f:
        balance = f.read()
        print("Your current balance is:", balance)


# Function to deposit money
def deposit():
    # Take deposit amount from user
    money_depo = int(input("Enter your deposit amount: "))

    # Read current balance from file
    with open("balance.txt", "r") as f:
        balance = int(f.read())

    # Add deposit amount to balance
    new_balance = balance + money_depo

    # Write updated balance back to file
    with open("balance.txt", "w") as f:
        f.write(str(new_balance))

    print("Deposit successful!")
    print("New balance:", new_balance)


# Function to withdraw money
def withdraw():
    # Take withdraw amount from user
    withdraw_amount = int(input("Enter your withdraw amount: "))

    # Read current balance
    with open("balance.txt", "r") as f:
        balance = int(f.read())

    print("Your balance is:", balance)

    # Check if withdraw amount is greater than balance
    if withdraw_amount > balance:
        print("Error: Insufficient balance")
        return
    else:
        new_balance = balance - withdraw_amount

    # Write remaining balance back to file
    with open("balance.txt", "w") as f:
        f.write(str(new_balance))

    print("Withdraw successful!")
    print("Remaining balance:", new_balance)


# Main program loop
while True:
    print("\n--- ATM MENU ---")
    print("1: Check balance")
    print("2: Deposit money")
    print("3: Withdraw money")
    print("4: Exit")

    user = int(input("Choose the option: "))

    if user == 1:
        get_balance()

    elif user == 2:
        deposit()

    elif user == 3:
        withdraw()

    elif user == 4:
        print("ATM closed")
        break

    else:
        print("Invalid option, please try again")
