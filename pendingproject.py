email="abc@gmail.com"
pwd=12345
otp=333
emailid=str(input('enter emailid:'))
password=int(input('enter password:'))
if(email==emailid):
    if(pwd==password):
        print('login successful')
        OTP=int(input('enter otp:'))
        if OTP == otp:
            print('logged into your account')
            def withdraw(account, amount):
                if len(account['transactions']) >= 5:
                    print('trancation limit exceeded')
                if amount > account['balance']:
                    print("Insufficient funds!")
                else:
                    account['balance'] -= amount
                    account['transactions'].append(f"Withdrawal: ${amount}")
                    print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

            def deposit(account, amount):
                account['balance'] += amount
                account['transactions'].append(f"Deposit: ${amount}")
                print(f"Deposit successful. Remaining balance: ${account['balance']}")

            def get_balance(account):
                return account['balance']

            def get_transaction_history(account):
                return account['transactions']

# Create an account dictionary
            account = {
            'balance': 1000,
            'transactions': []
             }

# Dictionary to map user choices to functions
             choices = {
             '1': deposit,
             '2': withdraw,
             '3': get_balance,
             '4': get_transaction_history
             }

             while True:
                 print("\n1. Deposit")
                 print("2. Withdraw")
                 print("3. Check Balance")
                 print("4. Transaction History")
                 print("5. Exit")

                 choice = input("Enter your choice: ")

                 if choice == '5':
                     print("Exiting program.")
                     break

                 if choice in choices:
                     if choice == '1':
                         amount = float(input("Enter amount: "))
                         choices[choice](account, amount)
                    if choice == '2' :
                        if account['transactions']!=5:
                            amount = float(input("Enter amount: "))
                            choices[choice](account, amount)
                        else:
                            print('transaction limit exceeded')
                    
                    else:
                       print(choices[choice](account))
            else:
                print("Invalid choice. Please try again.")
        else:
             print("Invalid otp. Please try again.")
                

    else:
        print('login failed incorrect password')
else:
    print('login failed incorrect emailid')