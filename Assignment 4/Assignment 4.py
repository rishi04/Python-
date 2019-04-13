"""
Created by Author: Rishikesh 'Richie' Maddi on Revision date: 2/8/19.
Email: rreddy67@gmail.com, rmadd2@unh.newhaven.edu
Program Summary: Program for SportShop for Mid term.
Copyright Ã‚Â© 2019 Richie. All rights reserved.
"""


class Person:
    # The class above describes a person with his First Name, Last Name and Account
    def __init__(self, firstname, lastname, account):
        self.first_name = firstname  # Public
        self.Last_name = lastname   # Public

        self.__Account = account  # private

    @property
    def print_fullname(self):
        """This is a function the full name of the person"""
        print('Full name  : ', self.first_name + self.Last_name)
        return ""

    def print_private(self):
        """this is the doc string of private attribute"""
        print('Account Number : ', self.__Account)
        return ""

    def set_account(self):
        """The docstring of setter"""
        return self.__Account

    def get_private(self):
        """the doc string of getter"""
        return self.__Account

    def __str__(self):
        return "Object information: " + str(self.__dict__)


class Account:

    def __init__(self, account_number, balance):
        self.Acc_No = account_number
        self.Acc_Bal = balance

    def withdrawal(self):
        if self.Acc_Bal > 0:
            user_input = input("Enter the amount you want to withdraw")
            amount = float(user_input)
            if amount > self.Acc_Bal:
                print("The amount is greater then your balance")
                breakpoint(0)
            self.Acc_Bal -= amount
            print(self.Acc_Bal)
        else:
            print("balance is zero, deposit money  to withdraw")
        return self.Acc_Bal

    def deposit(self):
        user_input = input("Enter the amount to deposit")
        amount = float(user_input)
        if amount < 1:
            print("The amount is to low")
        else:
            self.Acc_Bal += amount
        return self.Acc_Bal

    def __lt__(self, other):
        return self.Acc_Bal < other.Acc_Bal

    def display(self):
        print("\n Net Available Balance=", self.Acc_Bal)


class savings_Acc:

    def __init__(self, firstname, lastname, account_number, balance):
        self.first_name = firstname  # Public
        self.Last_name = lastname  # Public
        self.Acc_No = account_number
        self.Acc_Bal = balance

    def print_fullname(self):
        """This is a function the full name of the person"""
        print('Full name  : ', self.first_name + self.Last_name)
        return ""

    def deposit(self):
        user_input = input("Enter the amount to deposit")
        amount = float(user_input)
        if amount < 1:
            print("The amount is to low")
        else:
            self.Acc_Bal += amount
        return self.Acc_Bal


class checking_Acc:
    def __init__(self, firstname, lastname, account_number, balance):
        self.first_name = firstname  # Public
        self.Last_name = lastname  # Public
        self.Acc_No = account_number
        self.Acc_Bal = balance

    def print_fullname(self):
        """This is a function the full name of the person"""
        print('Full name  : ', self.first_name + self.Last_name)
        return ""

    def withdrawal(self):
        if self.Acc_Bal > 0:
            user_input = input("Enter the amount you want to withdraw")
            amount = float(user_input)
            if amount > self.Acc_Bal:
                print("The amount is greater then your balance")
                breakpoint(0)
            self.Acc_Bal -= amount
            print(self.Acc_Bal)
        else:
            print("balance is zero, deposit money  to withdraw")
        return self.Acc_Bal

    def deposit(self):
        user_input = input("Enter the amount to deposit")
        amount = float(user_input)
        if amount < 1:
            print("The amount is to low")
        else:
            self.Acc_Bal += amount
        return self.Acc_Bal

# First part of assignment


me = Person("Rishi", "Reddy", 1)
person = Person("Mithilesh", "Reddy", 2)

print('\n', me)
print('\n', person)
print(me.print_fullname)
print(me.print_private())
print(person.print_fullname)
print(person.print_private())
print(help(Person))

# Extension part of Assignment for Accounts

User1 = Account(1, 20)
User2 = Account(2, 25)
User3 = Account(3, 30)
User4 = Account(4, 42)
User5 = Account(5, 44)
User6 = Account(6, 201)
User7 = Account(7, 2045.2)
User8 = Account(8, 24.3)
User9 = Account(9, 92340)

customer_object = [User1, User2, User3, User4, User5, User6, User7, User8, User9]

customer_object.sort(key=lambda account: account.Acc_No)

for obj in customer_object:
    print("Sorted Account Number from obj: " + str(obj.Acc_Bal) + ": Along with  Account number: " + str(obj.Acc_No) + "\n")

# Last part of assignment for checking and savings account


new_account = input("\n Enter 1 to create savings account and 2 to create checking account:  ")


if new_account == "1":
    first_name = input("\n Enter the First name of the user: ")
    last_name = input("\n Enter the Last name of the user: ")
    acc_no = input("\nEnter new account number :")
    acc_bal = input("\n Enter the deposit amount")
    new_user = savings_Acc(first_name, last_name, acc_no, acc_bal)
elif new_account == "2":
    first_name = input("\n Enter the First name of the user: ")
    last_name = input("\n Enter the Last name of the user: ")
    acc_no = input("\nEnter new account number :")
    while True:
        acc_bal = input("\n Enter the deposit amount(A minimum of 250$)")
        if acc_bal >= "250":
            new_user = savings_Acc(first_name, last_name, acc_no, acc_bal)
            break
        else:
            print("Deposit amount is to low re-enter amount")

print("\n Thank you for using my program\n")
