print("(((((((( Welcome To Our ATM ))))))))")
print("Insert Your Card")

pin = 1234
totalAmount = 50000
accountNumber = 123456789

while True:
    print("\nSelect Your Option")
    print("1. Deposit\n2. Withdraw\n3. Balance Check\n")

    try:
        option = int(input("Select an option (1/2/3): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if option == 1:  # Deposit
        try:
            depositAmount = int(input("Enter Your Amount to Deposit: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if depositAmount > 0:
            try:
                depositPin = int(input("Enter Your PIN: "))
            except ValueError:
                print("Invalid PIN format!")
                continue

            if depositPin == pin:
                totalAmount += depositAmount
                print("Deposit Successful! Your New Balance:", totalAmount)
            else:
                print("Wrong PIN!")
        else:
            print("Invalid Deposit Amount!")

    elif option == 2:  # Withdraw
        print("Enter Your Amount Between 500 To 50000")
        print("\n1. 10,000\n2. 30,000\n3. 50,000\n4. Other Amount")

        try:
            withdrawOption = int(input("Select an option (1/2/3/4): "))
        except ValueError:
            print("Invalid input!")
            continue

        if withdrawOption == 1:
            withdrawAmount = 10000
        elif withdrawOption == 2:
            withdrawAmount = 30000
        elif withdrawOption == 3:
            withdrawAmount = 50000
        elif withdrawOption == 4:
            try:
                withdrawAmount = int(input("Enter Your Amount: "))
            except ValueError:
                print("Invalid amount format!")
                continue

            if withdrawAmount < 500 or withdrawAmount > 50000:
                print("Invalid Amount! Please withdraw between 500 and 50000.")
                continue
        else:
            print("Invalid Option!")
            continue

        try:
            withdrawPin = int(input("Enter Your PIN: "))
        except ValueError:
            print("Invalid PIN format!")
            continue

        if withdrawPin == pin:
            if withdrawAmount <= totalAmount:
                totalAmount -= withdrawAmount
                print("Collect Your Cash.")
                print("Remaining Balance:", totalAmount)
            else:
                print("Insufficient Balance!")
        else:
            print("Wrong PIN!")

    elif option == 3:  # Balance Check
        try:
            checkPin = int(input("Enter Your PIN: "))
        except ValueError:
            print("Invalid PIN format!")
            continue

        if checkPin == pin:
            print("Your Current Balance:", totalAmount)
        else:
            print("Wrong PIN!")

    else:
        print("Invalid Option! Please Try Again.")
