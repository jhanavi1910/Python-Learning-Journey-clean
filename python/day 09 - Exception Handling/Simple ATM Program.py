balance = 5000

while True:
    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Remaining Balance is:", balance)

        elif choice == 2:
            amt = int(input("Enter the amount to deposit: "))

            if amt > 0:
                balance = balance + amt
                print("Amount deposited successfully.")
                print("Remaining Balance is:", balance)
            else:
                print("Please enter a valid amount.")

        elif choice == 3:
            wd = int(input("Enter the amount to withdraw: "))

            if wd <= 0:
                print("Please enter a valid amount.")

            elif balance >= wd:
                balance = balance - wd
                print("Amount withdrawn successfully.")
                print("Remaining Balance is:", balance)

            else:
                print("Insufficient balance.")

        elif choice == 4:
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")

    except ValueError:
        print("Please enter integers only.")

    finally:
        print("Transaction Completed.")