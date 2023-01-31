# author: Paul Kim
# date: January 29, 2023
# version: 1.0
# This is a banking system prototype that allows the user to create and manage customer profiles and bank accounts


import datetime
import re

MIN_MAIN_MENU = 0
MAX_MAIN_MENU = 5
MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 60
MIN_BIRTH_YEAR = 1900
MAX_BIRTH_YEAR = datetime.date.today().year
MIN_BIRTH_MONTH = 1
MAX_BIRTH_MONTH = 12
MIN_BIRTH_DAY = 1
MAX_BIRTH_DAY1 = 31
MAX_BIRTH_DAY2 = 30
MAX_BIRTH_DAY_FEB = 28
MIN_ADDRESS_NUM = 0
MAX_ADDRESS_NUM = 999999
MIN_SEARCH_MENU = 0
MAX_SEARCH_MENU = 4

profile_list = []
accounts_list = []


class Account:
    def __init__(self, profile_num, account_num, account_type):
        self.profile_num = profile_num
        self.account_num = account_num
        self.account_type = account_type
        self.balance = 0
        self.timestamp = datetime.datetime.now()

    def display_details(self):
        print(
            f"        Account Number: {self.account_num} | Account Type: {self.account_type} | Balance: ${self.balance} | Create Date: {self.timestamp}")


class Profile:
    def __init__(self, profile_num, first_name, middle_name, last_name, date_of_birth, address, phone_num,
                 email_address):
        self.profile_num = profile_num
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_num = phone_num
        self.email_address = email_address

    def display_details(self):
        print(
            f"Profile Number: {self.profile_num} | First Name: {self.first_name} | Middle Name: {self.middle_name} | "
            f"Last Name: {self.last_name} | Date of Birth: {self.date_of_birth} | Address: {self.address} | "
            f"Phone Number : {self.phone_num} | Email: {self.email_address}")


def load_profile_data():
    global profile_list
    try:
        with open("profile_data.txt", "x+") as profile_data:
            file_content = profile_data.read()
            lines = file_content.splitlines()
            for line in lines:
                data = line.split(",")
                profile_num = data[0]
                first_name = data[1]
                middle_name = data[2]
                last_name = data[3]
                date_of_birth = data[4]
                address = data[5]
                phone_num = data[6]
                email_address = data[7]
                new_profile = Profile(profile_num, first_name, middle_name, last_name, date_of_birth, address,
                                      phone_num,
                                      email_address)
                profile_list.append(new_profile)
    except FileExistsError:
        try:
            with open("profile_data.txt", "r+") as profile_data:
                file_content = profile_data.read()
                lines = file_content.splitlines()
                for line in lines:
                    data = line.split(",")
                    profile_num = data[0]
                    first_name = data[1]
                    middle_name = data[2]
                    last_name = data[3]
                    date_of_birth = data[4]
                    address = data[5]
                    phone_num = data[6]
                    email_address = data[7]
                    new_profile = Profile(profile_num, first_name, middle_name, last_name, date_of_birth, address,
                                          phone_num, email_address)
                    profile_list.append(new_profile)
        except:
            profile_list = []
    except Exception:
        print("An unexpected error has occurred, please contact program developer. Ending program.")
        exit()


def load_accounts_data():
    global accounts_list
    try:
        with open("accounts_data_test.txt", "x+") as accounts_data:
            file_content = accounts_data.read()
            lines = file_content.splitlines()
            for line in lines:
                data1 = line.split(",")
                profile_num1 = data1[0]
                account_num = data1[1]
                account_type = data1[2]
                new_account = Account(profile_num1, account_num, account_type)
                new_account.balance += float(data1[3])
                new_account.timestamp = data1[4]
                accounts_list.append(new_account)
    except FileExistsError:
        try:
            with open("accounts_data_test.txt", "r+") as accounts_data:
                file_content = accounts_data.read()
                lines = file_content.splitlines()
                for line in lines:
                    data1 = line.split(",")
                    profile_num1 = data1[0]
                    account_num = data1[1]
                    account_type = data1[2]
                    new_account = Account(profile_num1, account_num, account_type)
                    new_account.balance += float(data1[3])
                    new_account.timestamp = data1[4]
                    accounts_list.append(new_account)
        except:
            accounts_list = []
    except Exception:
        print("An unexpected error has occurred, please contact program developer. Ending program.")
        exit()


load_profile_data()
load_accounts_data()


def create_first_name():
    print('Input "cancel" to cancel at any time')
    while True:
        first_name = input("Enter first name: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", first_name):
                raise ValueError
            elif len(first_name) < MIN_NAME_LENGTH or len(first_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid first name, must be between 1 and 60 characters")
        else:
            if first_name == "cancel":
                main_menu()
            else:
                return first_name


def create_middle_name():
    while True:
        middle_name = input("Enter middle name (optional)(input space to skip): ")
        try:
            if not re.search("^[A-Za-z-' ]+$", middle_name):
                raise ValueError
            elif len(middle_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid middle name, must be between 1 and 60 characters")
        else:
            if middle_name == "cancel":
                main_menu()
            else:
                return middle_name


def create_last_name():
    while True:
        last_name = input("Enter last name: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", last_name):
                raise ValueError
            elif len(last_name) < MIN_NAME_LENGTH or len(last_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid first name, must be between 1 and 60 characters")
        else:
            if last_name == "cancel":
                main_menu()
            else:
                return last_name


def create_date_of_birth():
    while True:
        birth_year = input("Enter birth year: ")
        if birth_year == "cancel":
            main_menu()
        else:
            try:
                birth_year = int(birth_year)
                if birth_year not in range(MIN_BIRTH_YEAR, MAX_BIRTH_YEAR + 1):
                    raise ValueError
            except ValueError:
                print("Invalid birth year, must be between 1900 and current year")
            else:
                break
    while True:
        birth_month = input("Enter birth month (1-12): ")
        if birth_month == "cancel":
            main_menu()
        else:
            try:
                birth_month = int(birth_month)
                if birth_month not in range(MIN_BIRTH_MONTH, MAX_BIRTH_MONTH + 1):
                    raise ValueError
            except ValueError:
                print("Invalid birth month, must be between 1 and 12")
            else:
                break
    while True:
        birth_day = input("Enter birth day (1-31): ")
        if birth_day == "cancel":
            main_menu()
        else:
            try:
                birth_day = int(birth_day)
                if int(birth_month) in [1, 3, 5, 7, 8, 10, 12]:
                    if birth_day not in range(MIN_BIRTH_DAY, MAX_BIRTH_DAY1 + 1):
                        raise ValueError
                elif int(birth_month) in [4, 6, 9, 11]:
                    if birth_day not in range(MIN_BIRTH_DAY, MAX_BIRTH_DAY2 + 1):
                        raise ValueError
                elif int(birth_month) == 2:
                    if birth_day not in range(MIN_BIRTH_DAY, MAX_BIRTH_DAY_FEB + 1):
                        raise ValueError
            except ValueError:
                print("Invalid birth day")
            else:
                date_of_birth = f"{birth_year}-{birth_month}-{birth_day}"
                return date_of_birth


def create_address():
    while True:
        unit_number = input("Enter unit number if applicable (input space if not): ")
        if unit_number == "cancel":
            main_menu()
        elif unit_number == ' ':
            break
        else:
            try:
                unit_number = int(unit_number)
                if unit_number not in range(MIN_ADDRESS_NUM, MAX_ADDRESS_NUM + 1):
                    raise ValueError
            except ValueError:
                print("Invalid unit number, must be between 0 and 999999")
            else:
                break
    while True:
        street_number = input("Enter street number: ")
        if street_number == "cancel":
            main_menu()
        else:
            try:
                street_number = int(street_number)
                if street_number not in range(MIN_ADDRESS_NUM, MAX_ADDRESS_NUM + 1):
                    raise ValueError
            except ValueError:
                print("Invalid unit number, must be between 0 and 999999")
            else:
                break
    while True:
        street_name = input("Enter street name: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", street_name):
                raise ValueError
            elif len(street_name) < MIN_NAME_LENGTH or len(street_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid street name, must be between 1 and 60 characters")
        else:
            if street_name == "cancel":
                main_menu()
            else:
                break
    while True:
        city = input("Enter city: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", city):
                raise ValueError
            elif len(city) < MIN_NAME_LENGTH or len(city) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid city, must be between 1 and 60 characters")
        else:
            if city == "cancel":
                main_menu()
            else:
                break
    while True:
        province = input("Enter province or state: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", province):
                raise ValueError
            elif len(province) < MIN_NAME_LENGTH or len(province) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid province, must be between 1 and 60 characters")
        else:
            if province == "cancel":
                main_menu()
            else:
                break
    while True:
        postal_code = input("Enter postal code: ")
        try:
            if not re.search("^[A-Za-z0-9-' ]+$", postal_code):
                raise ValueError
            elif len(postal_code) < MIN_NAME_LENGTH or len(postal_code) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid postal code, must be between 1 and 60 characters")
        else:
            if postal_code == "cancel":
                main_menu()
            else:
                break
    while True:
        country = input("Enter country: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", country):
                raise ValueError
            elif len(country) < MIN_NAME_LENGTH or len(country) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid province, must be between 1 and 60 characters")
        else:
            if country == "cancel":
                main_menu()
            else:
                address = f"{unit_number} {street_number} {street_name} {city} {province} {postal_code} {country}"
                return address


def create_phone_number():
    while True:
        phone_num = input("Enter phone number (format ###-###-####): ")
        if phone_num == 'cancel':
            main_menu()
        else:
            try:
                if not re.search("^[\d]{3}-[\d]{3}-[\d]{4}$", phone_num):
                    raise ValueError
            except ValueError:
                print("Invalid phone number, must be in format ###-###-####")
            else:
                return phone_num


def create_email_address():
    while True:
        email_address = input("Enter email address: ")
        if email_address == 'cancel':
            main_menu()
        else:
            try:
                if "@" not in email_address or "." not in email_address:
                    raise ValueError
            except ValueError:
                print("Invalid email address, please try again")
            else:
                return email_address


def profile_number_generator(input_list):
    if len(input_list) == 0:
        new_number = str(0).zfill(8)
    else:
        new_number = str(int(input_list[-1].profile_num) + 1).zfill(8)
    return new_number


def account_number_generator(input_list):
    if len(input_list) == 0:
        new_number = str(0).zfill(12)
    else:
        new_number = str(int(input_list[-1].account_num) + 1).zfill(12)
    return new_number


def create_account(input_profile):
    while True:
        print("""
        Banking System Prototype
        ====================
        Open New Account
        --------------------
        [1] Chequing
        [2] Saving
        [0] Cancel
        =====================
        Select account type
        """)
        user = input("Select account type (0-2): ")
        try:
            user = int(user)
            if user not in range(0, 3):
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            if user == 1:
                profile_num = input_profile.profile_num
                account_num = account_number_generator(accounts_list)
                account_type = "chequing"
                new_account = Account(profile_num, account_num, account_type)
                print("Account created successfully!")
                new_account.display_details()
                accounts_list.append(new_account)
                profile_menu(input_profile)
            elif user == 2:
                profile_num = input_profile.profile_num
                account_num = account_number_generator(accounts_list)
                account_type = "saving"
                new_account = Account(profile_num, account_num, account_type)
                print("Account created successfully!")
                new_account.display_details()
                accounts_list.append(new_account)
                profile_menu(input_profile)
            elif user == 0:
                return


def close_account(input_profile):
    user_del = input("Enter account number: ")
    for i in accounts_list:
        if i.account_num == user_del:
            if i.profile_num == input_profile.profile_num:
                confirm = input("Are you sure you want to delete?(1=yes 0=no): ")
                if confirm == '1':
                    accounts_list.remove(i)
                    print(f"Account {user_del} has been deleted.")
            else:
                print("This account does not belong to this profile owner.")


def display_accounts(input_list, input_profile):
    for i in input_list:
        if i.profile_num == input_profile.profile_num:
            i.display_details()


def account_menu(profile, account):
    while True:
        print(f"""
        Banking System Prototype
        ====================
        Profile # {profile.profile_num}
        Account # {account.account_num}
        Account Type : {account.account_type}
        Account Balance: ${account.balance}
        --------------------
        [1] Deposit
        [2] Withdrawal
        [3] Transfer Funds
        [0] Return to Profile Menu
        """)
        user = input("Please select an option: ")
        try:
            user = int(user)
            if user not in range(0, 4):
                raise ValueError
        except ValueError:
            print("Invalid input, please select a valid option")
        else:
            if user == 1:
                deposit = input("Enter deposit amount: ")
                try:
                    deposit = float(deposit)
                    if deposit < 0.01:
                        raise ValueError
                except ValueError:
                    print("Invalid amount")
                else:
                    account.balance += deposit
                    account_menu(profile, account)
            if user == 2:
                withdrawal = input("Enter withdrawal amount: ")
                try:
                    withdrawal = float(withdrawal)
                    if withdrawal > account.balance:
                        raise ValueError
                except ValueError:
                    print("Invalid amount")
                else:
                    account.balance -= withdrawal
                    account_menu(profile, account)
            if user == 3:
                while True:
                    funds = input("Enter amount to transfer: ")
                    try:
                        funds = int(funds)
                        if funds < 0 or funds > account.balance:
                            raise ValueError
                    except ValueError:
                        print("Invalid amount")
                    else:
                        break
                while True:
                    account1 = input("Enter account number to transfer to: ")
                    try:
                        if not re.search("^[\d]{12}$", account1):
                            raise ValueError
                    except ValueError:
                        print("Invalid account number")
                    else:
                        account.balance -= funds
                        for i in accounts_list:
                            if account1 == i.account_num:
                                i.balance += funds
                        account_menu(profile, account)

            if user == 0:
                profile_menu(profile)


def edit_profile(input_profile):
    while True:
        print(f"""
        Banking System Prototype
        ====================
        Profile # {input_profile.profile_num}
        --------------------
        [1] Edit First Name
        [2] Edit Middle Name
        [3] Edit Last Name
        [4] Edit Date of Birth
        [5] Edit Address
        [6] Edit Phone Number
        [7] Edit Email Address
        [0] Return to Profile
        """)
        user = input("Please select an option from above: ")
        try:
            user = int(user)
            if user not in range(0, 8):
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            if user == 1:
                new_first_name = create_first_name()
                input_profile.first_name = new_first_name
                profile_menu(input_profile)
            elif user == 2:
                new_middle_name = create_middle_name()
                input_profile.middle_name = new_middle_name
                profile_menu(input_profile)
            elif user == 3:
                new_last_name = create_last_name()
                input_profile.last_name = new_last_name
                profile_menu(input_profile)
            elif user == 4:
                new_date_of_birth = create_date_of_birth()
                input_profile.date_of_birth = new_date_of_birth
                profile_menu(input_profile)
            elif user == 5:
                new_address = create_address()
                input_profile.address = new_address
                profile_menu(input_profile)
            elif user == 6:
                new_phone_number = create_phone_number()
                input_profile.phone_num = new_phone_number
                profile_menu(input_profile)
            elif user == 7:
                new_email = create_email_address()
                input_profile.email_address = new_email
                profile_menu(input_profile)
            elif user == 0:
                profile_menu(input_profile)


def profile_menu(input_profile):
    while True:
        print(f"""
        Banking System Prototype
        ====================
        Profile # {input_profile.profile_num}
        --------------------
        First Name: {input_profile.first_name} Middle Name: {input_profile.middle_name} Last Name: {input_profile.last_name}
        Date of Birth: {input_profile.date_of_birth}
        Phone Number: {input_profile.phone_num} Email Address: {input_profile.email_address}
        Address: {input_profile.address}
        Accounts:""")
        display_accounts(accounts_list, input_profile)
        print(f"""
        ====================
        [1] Open new account
        [2] Choose existing account
        [3] Close account
        [4] Edit profile
        [0] Return to Main Menu
        """)
        user = input("Please select an option from above: ")
        try:
            user = int(user)
            if user not in range(0, 5):
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            if user == 1:
                create_account(input_profile)
            if user == 2:
                while True:
                    account = input("Enter account number: ")
                    if account == 'cancel':
                        return
                    try:
                        if not re.search("^[\d]{12}$", account):
                            raise ValueError
                    except ValueError:
                        print("Invalid account number")
                    else:
                        for i in accounts_list:
                            if i.account_num == account:
                                account_menu(input_profile, i)
            if user == 3:
                close_account(input_profile)
            if user == 4:
                edit_profile(input_profile)
            if user == 0:
                main_menu()


def search_by_profile_number(input_list):
    user = input("Enter profile number: ")
    for i in input_list:
        if user == i.profile_num:
            profile_menu(i)


def search_by_last_name(input_list):
    user = input("Enter last name: ")
    print("""
        Banking System Prototype
        ====================
        Search Profile
        --------------------""")
    for i in input_list:
        if user in i.last_name:
            print(
                f"Profile Number: {i.profile_num} | First Name: {i.first_name} | Middle Name: {i.middle_name} | Last Name: {i.last_name}")
    user_choice = input("Input profile number (-1 to cancel): ")
    try:
        if user_choice == '-1':
            main_menu()
        if not re.search("^[\d]{8}$", user_choice):
            raise ValueError
    except ValueError:
        print("Invalid input, please input a profile number")
    else:
        for i in profile_list:
            if i.profile_num == user_choice:
                profile_menu(i)


def search_by_phone_number(input_list):
    user = input("Enter phone number: ")
    for i in input_list:
        if user == i.phone_num:
            profile_menu(i)


def search_by_email(input_list):
    user = input("Enter email address: ")
    for i in input_list:
        if user == i.email_address:
            profile_menu(i)


def save_data(input_list1, input_list2):
    print("Saving data.")
    with open("profile_data.txt", "w") as profile_data:
        for i in input_list1:
            profile_data.write(
                f"{i.profile_num},{i.first_name},{i.middle_name},{i.last_name},{i.date_of_birth},{i.address},{i.phone_num},{i.email_address}\n")
    with open("accounts_data_test.txt", "w") as accounts_data:
        for j in input_list2:
            accounts_data.write(f"{j.profile_num},{j.account_num},{j.account_type},{j.balance},{j.timestamp}\n")


def search_profile_menu():
    while True:
        print("""
        Banking System Prototype
        ====================
        Search Profile
        --------------------
        [1] By profile number
        [2] By last name
        [3] By phone number
        [4] By email address
        [0] Return to Main Menu
        ====================
        Please select an option from above
        """)
        user = input("Please choose an option from the search menu (0-4): ")
        try:
            user = int(user)
            if user not in range(MIN_SEARCH_MENU, MAX_SEARCH_MENU + 1):
                raise ValueError
        except ValueError:
            print("Invalid input, please select an option from the search menu (0-4)")
        else:
            if user == 1:
                print("By profile number")
                search_by_profile_number(profile_list)
            elif user == 2:
                print("By last name")
                search_by_last_name(profile_list)
            elif user == 3:
                print("By phone number")
                search_by_phone_number(profile_list)
            elif user == 4:
                print("By email address")
                search_by_email(profile_list)
            elif user == 0:
                return


def delete_profile(input_list, input_list2):
    user_del = input("Enter profile number: ")
    for i in input_list:
        if user_del == i.profile_num:
            input_list.remove(i)
            print(f"Profile {user_del} has been deleted.")
    for j in input_list2:
        if user_del == j.profile_num:
            input_list.remove(j)
            print(f"All accounts associated with Profile {user_del} have been deleted.")


def display_profiles(input_list):
    for i in input_list:
        i.display_details()


def create_profile():
    profile_num = profile_number_generator(profile_list)
    first_name = create_first_name()
    middle_name = create_middle_name()
    last_name = create_last_name()
    date_of_birth = create_date_of_birth()
    address = create_address()
    phone_num = create_phone_number()
    email_address = create_email_address()
    new_profile = Profile(profile_num, first_name, middle_name, last_name, date_of_birth, address, phone_num,
                          email_address)
    return new_profile


def main_menu():
    while True:
        print("""
        Banking System Prototype
        ====================
        Main Menu
        --------------------
        [1] Create Profile
        [2] Display Profiles
        [3] Search Profile
        [4] Delete Profile
        [5] Save Data
        [0] Exit
        ====================
        Please select an option from above
        """)
        user = input("Please choose an option from the main menu (0-4): ")
        try:
            user = int(user)
            if user not in range(MIN_MAIN_MENU, MAX_MAIN_MENU + 1):
                raise ValueError
        except ValueError:
            print("Invalid input, please select an option from the main menu")
        else:
            if user == 1:
                print("Create Profile")
                new_profile = create_profile()
                print("Account created successfully!")
                new_profile.display_details()
                profile_list.append(new_profile)
            elif user == 2:
                print("Display Profiles")
                display_profiles(profile_list)
            elif user == 3:
                print("Search Profile")
                search_profile_menu()
            elif user == 4:
                print("Delete Profile")
                delete_profile(profile_list, accounts_list)
            elif user == 5:
                print("Save Data")
                save_data(profile_list, accounts_list)
            elif user == 0:
                exit_menu = input("Do you want to save changes? (1=yes, 0=no): ")
                try:
                    exit_menu = int(exit_menu)
                    if exit_menu not in range(0, 2):
                        raise ValueError
                except ValueError:
                    print("Invalid input, please select 1 for yes, 0 for no")
                else:
                    if exit_menu == 1:
                        save_data(profile_list, accounts_list)
                        print("Ending program.")
                        exit()
                    elif exit_menu == 0:
                        print("Ending program.")
                        exit()


def main():
    main_menu()


if __name__ == "__main__":
    main()
