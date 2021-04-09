# BANKONG APP
# 1. Class based
# 2. Should have methods for withdrawl and deposit
# 3. Write the transaction to the python file
# 4. App should keep asking user over and over again if he want to withdrawl or deposit
import random

print("SET UP YOUR NEW BANK ACCOUNT")

while True:
    account_holder_name = input("Please enter your name: ")
    if account_holder_name == "":
        print("You have to enter your name to open an account.")
        continue
    else:
        break

my_bank_name = input(
    f"{account_holder_name}, please enter name of the bank you want to open account with? ")
if my_bank_name == "":
    my_bank_name = "X Bank"


class Bank:
    bank_balance = 0
    your_currency = "$"
    account_number = ""
    transaction_num = 0

    def __init__(self, bank_name, account_name):
        self.bank_name = bank_name
        self.account_name = account_name

    def genAccNumber(self):
        acc_num = ""
        i = 0
        while i < 12:
            rnd = int(random.random() * 10)
            rnd = str(rnd)
            acc_num = acc_num + rnd
            i = i + 1
        return acc_num

    def makeDeposit(self, amount):
        self.transaction_num = self.transaction_num + 1
        self.bank_balance = round(self.bank_balance + amount, 2)
        print(f"{self.account_name}, you have deposited {self.your_currency}{amount}")
        print(f"Your new balance is: {self.your_currency}{self.bank_balance}")
        self.writeToFile(self.transaction_num, 'deposit', amount)

    def makeWithdrawal(self, amount):
        if amount > self.bank_balance:
            print(
                f"Your balance is too low. You can max withrow {self.bank_balance}")
        else:
            self.transaction_num = self.transaction_num + 1
            self.bank_balance = round(self.bank_balance - amount, 2)
            print(
                f"{self.account_name}, you have withdrown {self.your_currency}{amount}")
            print(
                f"Your new balance is: {self.your_currency}{self.bank_balance}")
            self.writeToFile(self.transaction_num, 'withdrawal', amount)

    def writeToFile(self, trans_num, trans_type, amount):
        with open('transactin_log.csv', 'a') as file:
            file.write(
                f'\n{trans_num},{trans_type},{amount},{self.bank_balance}')

    def createLogFile(self):
        with open('transactin_log.csv', 'w') as file:
            file.write(
                f'Account holder name: {self.account_name} \nBank name: {self.bank_name} \nAccount number: {self.account_number}\n')
            file.write(f'\nTrans number, Trans type,Amount,Total balance')


class MyBank(Bank):
    def __init__(self, bank_name, account_name):
        super().__init__(bank_name, account_name)
        self.your_currency = "£"


my_bank_account = MyBank(my_bank_name, account_holder_name)
my_bank_account.account_number = my_bank_account.genAccNumber()

print(
    f"Congratulations {my_bank_account.account_name}. Account in {my_bank_account.bank_name} bank has been open.")
print(f"Your new bank account number is: {my_bank_account.account_number}")
my_bank_account.createLogFile()

# my_bank_account.makeDeposit(600)
# my_bank_account.makeDeposit(125)
# my_bank_account.makeDeposit(258)
# my_bank_account.makeWithdrawal(350)
# my_bank_account.makeWithdrawal(62)
action_lst = ['d', 'w', 'q']

while True:
    action = input(
        "Select your option: D - deposit, W - withdrawal, Q - quit? ")
    if action.lower() not in action_lst:
        print(
            "Incorrect option selected. Try again! ")
        continue
    else:
        if action == 'd':
            deposit = input(
                f"How much would you like to deposit, {my_bank_account.account_name}? ")
            try:
                deposit = float(deposit)
                my_bank_account.makeDeposit(deposit)
            except:
                print(
                    f"{my_bank_account.account_name}, only number values are accepted.")
        elif action == 'w':
            withdrawal = input(
                f"How much would you like to withdraw, {my_bank_account.account_name}? ")
            try:
                withdrawal = float(withdrawal)
                my_bank_account.makeWithdrawal(withdrawal)
            except:
                print(
                    f"{my_bank_account.account_name}, only number values are accepted.")
        else:
            break
