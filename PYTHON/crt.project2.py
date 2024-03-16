#create an atm system
#displaying the reaming amount in atm
#select the card rupay-2k limit,visa-5k limit,mastercard-8klimit
#authenticate the user if the user is authenticated then
#giving the following option1 1.(check balance)
                            #2.(cash deposite)
                            #3.(cashwithdraw)
#mini statement of the last three transaction
from abc import ABC, abstractmethod

class ATM(ABC):
    base_balance = 50000  

    @abstractmethod
    def amount(self):
        print("Enter the amount:")
        print(amount)

class RuPay(ATM):
    def __init__(self, balance):
        self.balance = balance

    def amount(self):
        remaining_amount = ATM.base_balance - self.balance
        print("Displaying the remaining amount in ATM:", remaining_amount)
        print(f"Remaining balance for RuPay card:")


class Visa(ATM):
    def __init__(self, balance_visa):
        self.balance = balance

    def amount(self):
        remaining_amount = ATM.base_balance - self.balance
        print("Displaying the remaining amount in ATM:",remaining_amount)
        print(f"Remaining balance for Visa card:")


class Mastercard(ATM):
    def __init__(self):
        self.balance = balance

    def amount(self):
        remaining_amount = ATM.base_balance - self.balance
        print("Displaying the remaining amount in ATM:",remaining_amount)
        print(f"Remaining balance for Mastercard card:")

def create_atm_system():
    rupay_atm = RuPay(2000)
    visa_atm = Visa(5000)
    mastercard_atm = Mastercard(8000)
    while True:
        print("\nWelcome to the ATM!")
        print("1. Select RuPay Card (Limit: 2000)")
        print("2. Select Visa Card (Limit: 5000)")
        print("3. Select Mastercard (Limit: 8000)")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            card = rupay_atm
        elif choice == '2':
            card = visa_atm
        elif choice == '3':
            card = mastercard_atm
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        card.amount()

create_atm_system()

'''class ATM:
    def __init__(self, card_type, balance):
        self.card_type = card_type
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print("Withdrawal of {amount} successful. Remaining balance:{self.balance()}")
        def create_atm_system():
            rupay_atm = ATM("RuPay", 2000)
            visa_atm = ATM("Visa", 5000)
            mastercard_atm = ATM("Mastercard", 8000)
            while True:
                print("\nWelcome to the ATM!")
                print("1. Select RuPay Card (Limit: 2000)")
                print("2. Select Visa Card (Limit: 5000)")
                print("3. Select Mastercard (Limit: 8000)")
                print("4. Exit")
                a = int(input("Enter your choice: "))
                if a == 1:
                    card = rupay_atm
                elif a == 2:
                    card = visa_atm
                elif a == 3:
                    card = mastercard_atm
                elif a== 4:
                    print("Thank you for using our ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
obj=ATM("visa",7000)
obj.withdraw(6000)
obj.create_atm_system()'''





            
