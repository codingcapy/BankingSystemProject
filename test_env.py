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
MIN_ACCOUNT_MENU = 0
MAX_ACCOUNT_MENU = 3
MIN_EDIT_PROFILE_MENU = 0
MAX_EDIT_PROFILE_MENU = 7
MIN_CREATE_ACCOUNT_MENU = 0
MAX_CREATE_ACCOUNT_MENU = 2
MIN_PROFILE_MENU = 0
MAX_PROFILE_MENU = 4

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
        with open("profile_data.csv", "x+") as profile_data:
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
            with open("profile_data.csv", "r+") as profile_data:
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
        with open("accounts_data.csv", "x+") as accounts_data:
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
            with open("accounts_data.csv", "r+") as accounts_data:
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
    while True:
        first_name = input("Enter first name: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", first_name):
                raise ValueError
            elif len(first_name) < MIN_NAME_LENGTH or len(first_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid first name, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
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
            print(f"Invalid middle name, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
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
            print(f"Invalid first name, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return last_name


def create_birth_year():
    while True:
        birth_year = input("Enter birth year: ")
        if birth_year.lower() == "cancel":
            return "cancel"
        else:
            try:
                birth_year = int(birth_year)
                if birth_year not in range(MIN_BIRTH_YEAR, MAX_BIRTH_YEAR + 1):
                    raise ValueError
            except ValueError:
                print(f"Invalid birth year, must be between {MIN_BIRTH_YEAR} and {MAX_BIRTH_YEAR}")
            else:
                return birth_year


def create_birth_month():
    while True:
        birth_month = input(f"Enter birth month ({MIN_BIRTH_MONTH}-{MAX_BIRTH_MONTH}): ")
        if birth_month.lower() == "cancel":
            return "cancel"
        try:
            birth_month = int(birth_month)
            if birth_month not in range(MIN_BIRTH_MONTH, MAX_BIRTH_MONTH + 1):
                raise ValueError
        except ValueError:
            print("Invalid birth month, must be between 1 and 12")
        else:
            return birth_month


def create_birth_day(max_birth_day):
    while True:
        birth_day = input(f"Enter birth day ({MIN_BIRTH_DAY}-{max_birth_day}): ")
        if birth_day.lower() == "cancel":
            return "cancel"
        try:
            birth_day = int(birth_day)
            if birth_day not in range(MIN_BIRTH_DAY, max_birth_day + 1):
                raise ValueError
        except ValueError:
            print("Invalid birth day")
        else:
            return birth_day


def create_unit_number():
    while True:
        unit_number = input("Enter unit number (input space if not applicable): ")
        try:
            if len(unit_number) < MIN_ADDRESS_NUM or len(unit_number) > MAX_ADDRESS_NUM + 1:
                raise ValueError
        except ValueError:
            print(f"Invalid unit number, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return unit_number


def create_street_number():
    while True:
        street_number = input("Enter street number: ")
        try:
            if len(street_number) < MIN_ADDRESS_NUM or len(street_number) > MAX_ADDRESS_NUM + 1:
                raise ValueError
        except ValueError:
            print(f"Invalid street number, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return street_number


def create_street_name():
    while True:
        street_name = input("Enter street name (including street type e.g. Ave, St, Blvd): ")
        try:
            if not re.search("^[A-Za-z-' ]+$", street_name):
                raise ValueError
            elif len(street_name) < MIN_NAME_LENGTH or len(street_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid street name, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return street_name


def create_city():
    while True:
        city = input("Enter city: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", city):
                raise ValueError
            elif len(city) < MIN_NAME_LENGTH or len(city) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid city, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return city


def create_province():
    while True:
        province = input("Enter province or state: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", province):
                raise ValueError
            elif len(province) < MIN_NAME_LENGTH or len(province) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid province, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return province


def create_postal_code():
    while True:
        postal_code = input("Enter postal code: ")
        try:
            if not re.search("^[A-Za-z0-9-' ]+$", postal_code):
                raise ValueError
            elif len(postal_code) < MIN_NAME_LENGTH or len(postal_code) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid postal code, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return postal_code


def create_country():
    while True:
        country = input("Enter country: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", country):
                raise ValueError
            elif len(country) < MIN_NAME_LENGTH or len(country) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid province, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters")
        else:
            return country


def create_phone_number():
    while True:
        phone_num = input("Enter phone number (format ###-###-####): ")
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
        =====================""")
        user = input(f"Select account type ({MIN_CREATE_ACCOUNT_MENU}-{MAX_CREATE_ACCOUNT_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_CREATE_ACCOUNT_MENU, MAX_CREATE_ACCOUNT_MENU + 1):
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
                return
            elif user == 2:
                profile_num = input_profile.profile_num
                account_num = account_number_generator(accounts_list)
                account_type = "saving"
                new_account = Account(profile_num, account_num, account_type)
                print("Account created successfully!")
                new_account.display_details()
                accounts_list.append(new_account)
                return
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
        Account Menu
        --------------------
        Profile # {profile.profile_num}
        Account # {account.account_num}
        Account Type : {account.account_type}
        Account Balance: ${account.balance}
        --------------------
        [1] Deposit
        [2] Withdrawal
        [3] Transfer Funds
        [0] Return to Profile Menu
        ====================
        Please select an option from above
        """)
        user = input(f"Please choose an option from the account menu ({MIN_ACCOUNT_MENU}-{MAX_ACCOUNT_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_ACCOUNT_MENU, MAX_ACCOUNT_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the account menu ({MIN_ACCOUNT_MENU}-{MAX_ACCOUNT_MENU})")
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
                    return
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
                    return
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
                        return
            if user == 0:
                return


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
        ====================
        Please select an option from above
        """)
        user = input(f"Please select an option from the edit menu ({MIN_EDIT_PROFILE_MENU}-{MAX_EDIT_PROFILE_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_EDIT_PROFILE_MENU, MAX_EDIT_PROFILE_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the edit menu ({MIN_EDIT_PROFILE_MENU}-{MAX_EDIT_PROFILE_MENU})")
        else:
            if user == 1:
                new_first_name = create_first_name()
                input_profile.first_name = new_first_name
                return
            elif user == 2:
                new_middle_name = create_middle_name()
                input_profile.middle_name = new_middle_name
                return
            elif user == 3:
                new_last_name = create_last_name()
                input_profile.last_name = new_last_name
                return
            elif user == 4:
                new_birth_year = create_birth_year()
                new_birth_month = create_birth_month()
                if new_birth_month in [1, 3, 5, 7, 8, 10, 12]:
                    max_birth_day = 31
                elif new_birth_month in [4, 6, 9, 11]:
                    max_birth_day = 30
                elif new_birth_month == 2:
                    max_birth_day = 28
                new_birth_day = create_birth_day(max_birth_day)
                new_date_of_birth = f"{new_birth_year}-{new_birth_month}-{new_birth_day}"
                input_profile.date_of_birth = new_date_of_birth
                return
            elif user == 5:
                new_unit_number = create_unit_number()
                new_street_number = create_street_number()
                new_street_name = create_street_name()
                new_city = create_city()
                new_province = create_province()
                new_postal_code = create_postal_code()
                new_city = create_city()
                new_country = create_country()
                new_address = f"{new_unit_number} {new_street_number} {new_street_name} {new_city} {new_province} {new_postal_code} {new_country}"
                input_profile.address = new_address
                return
            elif user == 6:
                new_phone_number = create_phone_number()
                input_profile.phone_num = new_phone_number
                return
            elif user == 7:
                new_email = create_email_address()
                input_profile.email_address = new_email
                return
            elif user == 0:
                return


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
        --------------------
        [1] Open new account
        [2] Choose existing account
        [3] Close account
        [4] Edit profile
        [0] Return to Search Menu
        ====================
        Please select an option from above
        """)
        user = input(f"Please select an option from the profile menu ({MIN_PROFILE_MENU}-{MAX_PROFILE_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_PROFILE_MENU, MAX_PROFILE_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the profile menu ({MIN_PROFILE_MENU}-{MAX_PROFILE_MENU})")
        else:
            if user == 1:
                create_account(input_profile)
            if user == 2:
                account = input("Enter account number: ")
                for i in accounts_list:
                    if i.account_num == account:
                        account_menu(input_profile, i)
            if user == 3:
                close_account(input_profile)
            if user == 4:
                edit_profile(input_profile)
            if user == 0:
                return


def search_by_profile_number(input_list, low, high, input_search):
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].profile_num == input_search:
            profile_menu(input_list[mid])
            return
        elif input_list[mid].profile_num > input_search:
            return search_by_profile_number(input_list, low, mid - 1, input_search)
        else:
            return search_by_profile_number(input_list, mid + 1, high, input_search)
    else:
        return "Profile not found"


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
            return
        if not re.search("^[\d]{8}$", user_choice):
            raise ValueError
    except ValueError:
        print("Invalid input, please input a profile number")
    else:
        for i in profile_list:
            if i.profile_num == user_choice:
                profile_menu(i)
                break;


def search_by_phone_number(input_list, low, high, input_search):
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].phone_num == input_search:
            profile_menu(input_list[mid])
        elif input_list[mid].phone_num > input_search:
            return search_by_phone_number(input_list, low, mid - 1, input_search)
        else:
            return search_by_phone_number(input_list, mid + 1, high, input_search)
    else:
        return "Profile not found"


def search_by_email(input_list, low, high, input_search):
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].email_address == input_search:
            profile_menu(input_list[mid])
        elif input_list[mid].email_address > input_search:
            return search_by_email(input_list, low, mid - 1, input_search)
        else:
            return search_by_email(input_list, mid + 1, high, input_search)
    else:
        return "Profile not found"


def save_data(input_list1, input_list2):
    print("Saving data.")
    with open("profile_data.csv", "w") as profile_data:
        for i in input_list1:
            profile_data.write(
                f"{i.profile_num},{i.first_name},{i.middle_name},{i.last_name},{i.date_of_birth},{i.address},{i.phone_num},{i.email_address}\n")
    with open("accounts_data.csv", "w") as accounts_data:
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
        user = input(f"Please choose an option from the search menu ({MIN_SEARCH_MENU}-{MAX_SEARCH_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_SEARCH_MENU, MAX_SEARCH_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the search menu ({MIN_SEARCH_MENU}-{MAX_SEARCH_MENU})")
        else:
            if user == 1:
                print("By profile number")
                user = input("Enter profile number: ")
                search_by_profile_number(profile_list, 0, len(profile_list) - 1, user)
            elif user == 2:
                print("By last name")
                search_by_last_name(profile_list)
            elif user == 3:
                print("By phone number")
                user = input("Enter phone number: ")
                search_by_phone_number(profile_list, 0, len(profile_list) - 1, user)
            elif user == 4:
                print("By email address")
                user = input("Enter email address: ")
                search_by_email(profile_list, 0, len(profile_list) - 1, user)
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


def create_profile(input_list):
    print('Input "cancel" to cancel at any time')
    profile_num = profile_number_generator(profile_list)
    first_name = create_first_name()
    if first_name.lower() == "cancel":
        return
    middle_name = create_middle_name()
    if middle_name.lower() == "cancel":
        return
    last_name = create_last_name()
    if last_name.lower() == "cancel":
        return
    birth_year = create_birth_year()
    if birth_year == "cancel":
        return
    birth_month = create_birth_month()
    if birth_month == "cancel":
        return
    if birth_month in [1, 3, 5, 7, 8, 10, 12]:
        max_birth_day = MAX_BIRTH_DAY1
    elif birth_month in [4, 6, 9, 11]:
        max_birth_day = MAX_BIRTH_DAY2
    elif birth_month == 2:
        max_birth_day = MAX_BIRTH_DAY_FEB
    birth_day = create_birth_day(max_birth_day)
    if birth_day == "cancel":
        return
    date_of_birth = f"{birth_year}-{birth_month}-{birth_day}"
    unit_number = create_unit_number()
    if unit_number.lower() == "cancel":
        return
    street_number = create_street_number()
    if street_number.lower() == "cancel":
        return
    street_name = create_street_name()
    if street_name.lower() == "cancel":
        return
    city = create_city()
    if city.lower() == "cancel":
        return
    province = create_province()
    if province.lower() == "cancel":
        return
    postal_code = create_postal_code()
    if postal_code.lower() == "cancel":
        return
    country = create_country()
    if country.lower() == "cancel":
        return
    address = f"{unit_number} {street_number} {street_name} {city} {province} {postal_code} {country}"
    phone_num = create_phone_number()
    if phone_num.lower() == "cancel":
        return
    email_address = create_email_address()
    if email_address.lower() == "cancel":
        return
    new_profile = Profile(profile_num, first_name, middle_name, last_name, date_of_birth, address, phone_num,
                          email_address)
    print("Account created successfully!")
    new_profile.display_details()
    input_list.append(new_profile)


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
        user = input(f"Please choose an option from the main menu ({MIN_MAIN_MENU}-{MAX_MAIN_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_MAIN_MENU, MAX_MAIN_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the main menu ({MIN_MAIN_MENU}-{MAX_MAIN_MENU})")
        else:
            if user == 1:
                print("Create Profile")
                create_profile(profile_list)
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
