
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
def deposit():
    amount = float(input("Enter amount to be deposited: "))

    if amount < 0:
        print("Amount cannot be negative.")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient Balance.")
        return 0
    elif amount < 0:
        print("Amount can not be negative.")
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("-------------------")
        print(" Banking Program.")
        print("-------------------")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter Your choice(1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("-------------------")
            print("  Invalid choice.")
            print("-------------------")
        print()
    print("------------------------------")
    print("  Thank you! Visit again :)")
    print("------------------------------")
    return None
main()