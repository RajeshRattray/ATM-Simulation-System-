class ATM:
    def __init__(self):
        self.balance = 2000.0  # Initial balance
        self.pin = "1000"  # Default PIN
        self.transactions = []  # List to store transaction history

    def validate_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        print("Too many incorrect attempts. Exiting.")
        return False

    def cash_withdrawal(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
            print(f"Please take your cash: ${amount}")
        else:
            print("Insufficient balance.")

    def balance_inquiry(self):
        print(f"Your current balance is: ${self.balance}")

    def pin_change(self):
        new_pin = input("Enter new PIN: ")
        self.pin = new_pin
        print("PIN changed successfully.")

    def mini_statement(self):
        print("Recent Transactions:")
        for transaction in self.transactions:
            print(transaction)

    def cash_deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
        print(f"Successfully deposited: ${amount}")

    def fund_transfer(self):
        amount = float(input("Enter amount to transfer: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Transferred: ${amount}")
            print(f"Successfully transferred: ${amount}")
        else:
            print("Insufficient balance.")

    def bill_payment(self):
        amount = float(input("Enter bill amount: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Bill paid: ${amount}")
            print(f"Bill payment of ${amount} successful.")
        else:
            print("Insufficient balance.")

    def cheque_book_request(self):
        print("Cheque book requested successfully.")

    def mobile_recharge(self):
        amount = float(input("Enter recharge amount: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Mobile recharge: ${amount}")
            print(f"Mobile recharged with: ${amount}")
        else:
            print("Insufficient balance.")

    def aadhaar_seeding(self):
        aadhaar_number = input("Enter your Aadhaar number: ")
        print(f"Aadhaar number {aadhaar_number} linked successfully.")

    def account_information(self):
        print("Account Information: Balance: ${}".format(self.balance))

    def atm_menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Cash Withdrawal")
            print("2. Balance Inquiry")
            print("3. PIN Change")
            print("4. Mini Statement")
            print("5. Cash Deposit")
            print("6. Fund Transfer")
            print("7. Bill Payment")
            print("8. Cheque Book Request")
            print("9. Mobile Recharge")
            print("10. Aadhaar Seeding")
            print("11. Account Information")
            print("12. Exit")

            choice = input("Select an option: ")

            if choice == '12':
                print("Thank you for using the ATM. Goodbye!")
                break

            if self.validate_pin():
                if choice == '1':
                    self.cash_withdrawal()
                elif choice == '2':
                    self.balance_inquiry()
                elif choice == '3':
                    self.pin_change()
                elif choice == '4':
                    self.mini_statement()
                elif choice == '5':
                    self.cash_deposit()
                elif choice == '6':
                    self.fund_transfer()
                elif choice == '7':
                    self.bill_payment()
                elif choice == '8':
                    self.cheque_book_request()
                elif choice == '9':
                    self.mobile_recharge()
                elif choice == '10':
                    self.aadhaar_seeding()
                elif choice == '11':
                    self.account_information()
                else:
                    print("Invalid option. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.atm_menu()
