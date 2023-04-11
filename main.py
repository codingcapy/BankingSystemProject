# Author: capytech
# Date: April 10, 2023
# Version: 2.0
# This program is a Banking System Prototype that allows user to create, edit, search, delete profiles and accounts
# and perform account transactions

import datetime
import re

MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 60
MIN_BIRTH_YEAR = 1900
MAX_BIRTH_YEAR = datetime.datetime.today().year
MIN_BIRTH_MONTH = 1
MAX_BIRTH_MONTH = 12
MIN_BIRTH_DAY = 1
MIN_PHONE_NUMBER_LENGTH = 4
MAX_PHONE_NUMBER_LENGTH = 15
MIN_EMAIL_ADDRESS_LENGTH = 5
MAX_EMAIL_ADDRESS_LENGTH = 255
CHQ_ACCT_INTEREST_RATE = 0.0
SAV_ACCT_INTEREST_RATE = 5.0
MIN_MAIN_MENU = 0
MAX_MAIN_MENU = 4
MIN_DISPLAY_MENU = 0
MAX_DISPLAY_MENU = 3
MIN_SEARCH_MENU = 0
MAX_SEARCH_MENU = 3
MIN_PROFILE_MENU_ACTIVE = 0
MAX_PROFILE_MENU_ACTIVE = 4
MIN_PROFILE_MENU_INACTIVE = 0
MAX_PROFILE_MENU_INACTIVE = 1
MIN_EDIT_MENU = 0
MAX_EDIT_MENU = 7
MIN_ACCOUNT_MENU_ACTIVE = 0
MAX_ACCOUNT_MENU_ACTIVE = 3
MIN_ACCOUNT_MENU_INACTIVE = 0
MAX_ACCOUNT_MENU_INACTIVE = 1
MIN_CREATE_ACCT_MENU = 0
MAX_CREATE_ACCT_MENU = 2


class Profile:
    def __init__(self, profile_number, first_name, middle_name, last_name, date_of_birth, address, phone_number,
                 email_address, status):
        self.profile_number = profile_number
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address
        self.status = status

    def display_details(self):
        print(
            f"{self.profile_number} {self.first_name} {self.middle_name} {self.last_name} {self.date_of_birth} {self.address} {self.phone_number} {self.email_address} {self.status}")

    def format_data(self):
        return f"{self.profile_number},{self.first_name},{self.middle_name},{self.last_name},{self.date_of_birth},{self.address},{self.phone_number},{self.email_address},{self.status}\n"


class Account:
    def __init__(self, profile_number, account_number, account_type, interest_rate, balance, status):
        self.profile_number = profile_number
        self.account_number = account_number
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.balance = balance
        self.status = status

    def display_details(self):
        print(
            f"\t\t{self.profile_number} {self.account_number} {self.account_type} {self.interest_rate} {self.balance} {self.status}")

    def format_data(self):
        return f"{self.profile_number},{self.account_number},{self.account_type},{self.interest_rate},{self.balance},{self.status}\n"


profiles_list = []
accounts_list = []


def load_profiles_data():
    try:
        with open("profiles.csv", "x+") as profiles_data:
            file_content = profiles_data.read()
            lines = file_content.splitlines()
            for line in lines:
                profile_data = line.split(",")
                profile_number = profile_data[0]
                first_name = profile_data[1]
                middle_name = profile_data[2]
                last_name = profile_data[3]
                date_of_birth = profile_data[4]
                address = profile_data[5]
                phone_number = profile_data[6]
                email_address = profile_data[7]
                status = profile_data[8]
                loaded_profile = Profile(profile_number, first_name, middle_name, last_name, date_of_birth, address,
                                         phone_number, email_address, status)
                profiles_list.append(loaded_profile)
    except FileExistsError:
        try:
            with open("profiles.csv", "r+") as profiles_data:
                file_content = profiles_data.read()
                lines = file_content.splitlines()
                for line in lines:
                    profile_data = line.split(",")
                    profile_number = profile_data[0]
                    first_name = profile_data[1]
                    middle_name = profile_data[2]
                    last_name = profile_data[3]
                    date_of_birth = profile_data[4]
                    address = profile_data[5]
                    phone_number = profile_data[6]
                    email_address = profile_data[7]
                    status = profile_data[8]
                    loaded_profile = Profile(profile_number, first_name, middle_name, last_name, date_of_birth, address,
                                             phone_number, email_address, status)
                    profiles_list.append(loaded_profile)
        except Exception as e:
            print(e)
    except Exception as e2:
        print(e2)


def load_accounts_data():
    try:
        with open("accounts.csv", "x+") as accounts_data:
            file_content = accounts_data.read()
            lines = file_content.splitlines()
            for line in lines:
                accounts_data = line.split(",")
                profile_number = accounts_data[0]
                account_number = accounts_data[1]
                account_type = accounts_data[2]
                interest_rate = float(accounts_data[3])
                balance = float(accounts_data[4])
                status = accounts_data[5]
                loaded_account = Account(profile_number, account_number, account_type, interest_rate, balance, status)
                accounts_list.append(loaded_account)
    except FileExistsError:
        try:
            with open("accounts.csv", "r+") as accounts_data:
                file_content = accounts_data.read()
                lines = file_content.splitlines()
                for line in lines:
                    accounts_data = line.split(",")
                    profile_number = accounts_data[0]
                    account_number = accounts_data[1]
                    account_type = accounts_data[2]
                    interest_rate = float(accounts_data[3])
                    balance = float(accounts_data[4])
                    status = accounts_data[5]
                    loaded_account = Account(profile_number, account_number, account_type, interest_rate, balance,
                                             status)
                    accounts_list.append(loaded_account)
        except Exception as e:
            print(e)
    except Exception as e2:
        print(e2)


load_profiles_data()
load_accounts_data()


def generate_profile_number(input_list):
    if len(input_list) == 0:
        new_number = str(0).zfill(8)
    else:
        new_number = str(int(input_list[-1].profile_number) + 1).zfill(8)
    return new_number


def generate_account_number(input_list):
    if len(input_list) == 0:
        new_number = str(0).zfill(12)
    else:
        new_number = str(int(input_list[-1].account_number) + 1).zfill(12)
    return new_number


def create_first_name():
    while True:
        first_name = input("Enter first name: ")
        try:
            if not re.search("^[A-Za-z-' ]+$", first_name):
                raise ValueError
            elif len(first_name) < MIN_NAME_LENGTH or len(first_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid first name, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
        else:
            return first_name


def create_middle_name():
    while True:
        middle_name = input("Enter middle name (input space if not applicable): ")
        try:
            if not re.search("^[A-Za-z-' ]+$", middle_name):
                raise ValueError
            elif len(middle_name) < MIN_NAME_LENGTH or len(middle_name) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid middle name, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
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
            print(f"Invalid last name, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
        else:
            return last_name


def create_birth_year():
    while True:
        birth_year = input("Enter birth year: ")
        if birth_year == "cancel":
            return "cancel"
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
        birth_month = input("Enter birth month: ")
        if birth_month == "cancel":
            return "cancel"
        try:
            birth_month = int(birth_month)
            if birth_month not in range(MIN_BIRTH_MONTH, MAX_BIRTH_MONTH + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid birth month, must be between {MIN_BIRTH_MONTH} and {MAX_BIRTH_MONTH}")
        else:
            return birth_month


def create_birth_day(max_birth_day):
    while True:
        birth_day = input("Enter birth day: ")
        if birth_day == "cancel":
            return "cancel"
        try:
            birth_day = int(birth_day)
            if birth_day not in range(MIN_BIRTH_DAY, max_birth_day + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid birth day, must be between {MIN_BIRTH_DAY} and {max_birth_day}")
        else:
            return birth_day


def create_street_address():
    while True:
        street_address = input("Enter street address (unit # st # st name st type): ")
        try:
            if not re.search("^[0-9A-Za-z-' ]+$", street_address):
                raise ValueError
            elif len(street_address) < MIN_NAME_LENGTH or len(street_address) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid street address, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
        else:
            return street_address


def create_city():
    while True:
        city = input("Enter city: ")
        try:
            if not re.search("^[0-9A-Za-z-' ]+$", city):
                raise ValueError
            elif len(city) < MIN_NAME_LENGTH or len(city) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid city, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
        else:
            return city


def create_province():
    while True:
        province = input("Enter province: ")
        try:
            if not re.search("^[0-9A-Za-z-' ]+$", province):
                raise ValueError
            elif len(province) < MIN_NAME_LENGTH or len(province) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid province, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
        else:
            return province


def create_postal_code():
    while True:
        postal_code = input("Enter postal code: ")
        try:
            if not re.search("^[0-9A-Za-z-' ]+$", postal_code):
                raise ValueError
            elif len(postal_code) < MIN_NAME_LENGTH or len(postal_code) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid postal code, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
        else:
            return postal_code


def create_country():
    while True:
        country = input("Enter country: ")
        try:
            if not re.search("^[0-9A-Za-z-' ]+$", country):
                raise ValueError
            elif len(country) < MIN_NAME_LENGTH or len(country) > MAX_NAME_LENGTH:
                raise ValueError
        except ValueError:
            print(f"Invalid country, must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters.")
        else:
            return country


def create_phone_number():
    while True:
        phone_number = input("Enter phone_number: ")
        if phone_number == "cancel":
            return "cancel"
        try:
            if not re.search("^[\d]+$", phone_number):
                raise ValueError
            elif len(phone_number) < MIN_PHONE_NUMBER_LENGTH or len(phone_number) > MAX_PHONE_NUMBER_LENGTH:
                raise ValueError
        except ValueError:
            print(
                f"Invalid phone number, must be between {MIN_PHONE_NUMBER_LENGTH} and {MAX_PHONE_NUMBER_LENGTH} numbers")
        else:
            return phone_number


def create_email_address():
    while True:
        email_address = input("Enter email address: ")
        if email_address == "cancel":
            return "cancel"
        try:
            if '@' not in email_address or "." not in email_address:
                raise ValueError
            elif len(email_address) < MIN_EMAIL_ADDRESS_LENGTH or len(email_address) > MAX_EMAIL_ADDRESS_LENGTH:
                raise ValueError
        except ValueError:
            print("Invalid email address, please try again.")
        else:
            return email_address


def create_profile():
    print('Input "cancel" at any time to cancel.')
    profile_number = generate_profile_number(profiles_list)
    first_name = create_first_name()
    if first_name == "cancel":
        return
    middle_name = create_middle_name()
    if middle_name == "cancel":
        return
    last_name = create_last_name()
    if last_name == "cancel":
        return
    birth_year = create_birth_year()
    if birth_year == "cancel":
        return
    birth_month = create_birth_month()
    if birth_month == "cancel":
        return
    if birth_month in [1, 3, 5, 7, 8, 10, 12]:
        max_birth_day = 31
    elif birth_month in [4, 6, 9, 11]:
        max_birth_day = 30
    elif birth_month == 2:
        max_birth_day = 28
    birth_day = create_birth_day(max_birth_day)
    if birth_day == "cancel":
        return
    date_of_birth = f"{birth_year}-{birth_month}-{birth_day}"
    street_address = create_street_address()
    if street_address == "cancel":
        return
    city = create_city()
    if city == "cancel":
        return
    province = create_province()
    if province == "cancel":
        return
    postal_code = create_postal_code()
    if postal_code == "cancel":
        return
    country = create_country()
    if country == "cancel":
        return
    phone_number = create_phone_number()
    if phone_number == "cancel":
        return
    email_address = create_email_address()
    if email_address == "cancel":
        return
    address = f"{street_address} {city} {province} {postal_code} {country}"
    status = "ACTIVE"
    new_profile = Profile(profile_number, first_name, middle_name, last_name, date_of_birth, address, phone_number,
                          email_address, status)
    print("Profile created successfully!")
    new_profile.display_details()
    profiles_list.append(new_profile)


def display_profiles_by_profile_number(input_list):
    input_list.sort(key=lambda x: x.profile_number)
    for i in input_list:
        i.display_details()


def display_profiles_by_last_name(input_list):
    input_list.sort(key=lambda x: x.last_name)
    for i in input_list:
        i.display_details()


def display_profiles_by_date_of_birth(input_list):
    input_list.sort(key=lambda x: x.date_of_birth)
    for i in input_list:
        i.display_details()


def create_account(profile):
    profile_number = profile.profile_number
    account_number = generate_account_number(accounts_list)
    balance = 0.0
    status = "ACTIVE"
    while True:
        print(f"""
        Banking System Prototype
        ====================
        Create Account Menu
        --------------------
        [1] Chequing
        [2] Saving
        [0] Return to Profile Menu
        ====================""")
        user = input(f"Please select an option from the menu ({MIN_CREATE_ACCT_MENU}-{MAX_CREATE_ACCT_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_CREATE_ACCT_MENU, MAX_CREATE_ACCT_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the menu ({MIN_CREATE_ACCT_MENU}-{MAX_CREATE_ACCT_MENU})")
        else:
            if user == 1:
                account_type = "chequing"
                interest_rate = CHQ_ACCT_INTEREST_RATE
                new_account = Account(profile_number, account_number, account_type, interest_rate, balance, status)
                print("Account created successfully!")
                accounts_list.append(new_account)
                return
            elif user == 2:
                account_type = "saving"
                interest_rate = SAV_ACCT_INTEREST_RATE
                new_account = Account(profile_number, account_number, account_type, interest_rate, balance, status)
                print("Account created successfully!")
                accounts_list.append(new_account)
                return
            elif user == 0:
                return


def deposit(account):
    while True:
        deposit_amt = input("Enter amount to deposit: ")
        if deposit_amt == "cancel":
            return
        try:
            deposit_amt = float(deposit_amt)
            if deposit_amt < 0:
                raise ValueError
        except ValueError:
            print("Invalid deposit amount")
        else:
            account.balance += deposit_amt
            print("Deposit successful")
            return


def withdraw(account):
    while True:
        withdrawal_amt = input("Enter amount to withdraw: ")
        if withdrawal_amt == "cancel":
            return
        try:
            withdrawal_amt = float(withdrawal_amt)
            if withdrawal_amt > account.balance:
                raise ValueError
        except ValueError:
            print("Invalid withdrawal amount")
        else:
            account.balance -= withdrawal_amt
            print("Withdrawal successful")
            return


def transfer(account):
    while True:
        transfer_amt = input("Enter transfer amount: ")
        if transfer_amt == "cancel":
            return
        try:
            transfer_amt = float(transfer_amt)
            if transfer_amt > account.balance:
                raise ValueError
        except ValueError:
            print("Invalid withdrawal amount")
        else:
            transfer_acct = input("Enter account to transfer to: ")
            if transfer_acct == "cancel":
                return
            else:
                transfer_search(account, accounts_list, 0, len(accounts_list) - 1, transfer_amt, transfer_acct)
                return


def transfer_search(account, input_list, low, high, transfer_amt, transfer_acct):
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].account_number == transfer_acct:
            account.balance -= transfer_amt
            input_list[mid].balance += transfer_amt
            print("Transfer successful")
            return
        elif input_list[mid].account_number > transfer_acct:
            return transfer_search(account, input_list, low, mid -1, transfer_amt, transfer_acct)
        else:
            return transfer_search(account, input_list, mid + 1, high, transfer_amt, transfer_acct)
    else:
        print("Account not found")
        return


def account_menu(account):
    if account.status == "ACTIVE":
        while True:
            print(f"""
            Banking System Prototype
            ====================
            Account Menu
            --------------------
            Profile Number: {account.profile_number}
            Account Number: {account.account_number}
            Account Type: {account.account_type}
            Interest Rate: {account.interest_rate}
            Balance: ${account.balance}
            --------------------
            [1] Deposit
            [2] Withdraw
            [3] Transfer
            [0] Return to Profile Menu
            ====================""")
            user = input(f"Please select an option from the menu ({MIN_ACCOUNT_MENU_ACTIVE}-{MAX_ACCOUNT_MENU_ACTIVE}): ")
            try:
                user = int(user)
                if user not in range(MIN_ACCOUNT_MENU_ACTIVE, MAX_ACCOUNT_MENU_ACTIVE + 1):
                    raise ValueError
            except ValueError:
                print(f"Invalid input, please select an option from the menu ({MIN_ACCOUNT_MENU_ACTIVE}-{MAX_ACCOUNT_MENU_ACTIVE})")
            else:
                if user == 1:
                    deposit(account)
                elif user == 2:
                    withdraw(account)
                elif user == 3:
                    transfer(account)
                if user == 0:
                    return
    else:
        while True:
            print(f"""
            Banking System Prototype
            ====================
            Account Menu
            --------------------
            Profile Number: {account.profile_number}
            Account Number: {account.account_number}
            Account Type: {account.account_type}
            Interest Rate: {account.interest_rate}
            Balance: ${account.balance}
            --------------------
            [1] Reactivate account
            [0] Return to Profile Menu
            ====================""")
            user = input(f"Please select an option from the menu ({MIN_ACCOUNT_MENU_INACTIVE}-{MAX_ACCOUNT_MENU_INACTIVE}): ")
            try:
                user = int(user)
                if user not in range(MIN_ACCOUNT_MENU_INACTIVE, MAX_ACCOUNT_MENU_INACTIVE + 1):
                    raise ValueError
            except ValueError:
                print(f"Invalid input, please select an option from the menu ({MIN_ACCOUNT_MENU_INACTIVE}-{MAX_ACCOUNT_MENU_INACTIVE})")
            else:
                if user == 1:
                    account.status = "ACTIVE"
                    print("Account reactivated")
                    return
                if user == 0:
                    return


def select_account(input_list, low, high, input_search, profile):
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].account_number == input_search and input_list[mid].profile_number == profile.profile_number:
            account_menu(input_list[mid])
        elif input_list[mid].account_number > input_search:
            return select_account(input_list, low, mid - 1, input_search, profile)
        else:
            return select_account(input_list, mid + 1, high, input_search, profile)
    else:
        print("Account not found")


def delete_account(input_list, low, high, input_search, profile):
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].account_number == input_search and input_list[mid].profile_number == profile.profile_number:
            input_list[mid].status = "INACTIVE"
            print("Account deactivated successfully")
        elif input_list[mid].account_number > input_search:
            return select_account(input_list, low, mid - 1, input_search, profile)
        else:
            return select_account(input_list, mid + 1, high, input_search, profile)
    else:
        print("Account not found")


def edit_profile(profile):
    while True:
        print(f"""
        Banking System Prototype
        ====================
        Edit Profile
        --------------------
        [1] Edit first name
        [2] Edit middle name
        [3] Edit last name
        [4] Edit date of birth
        [5] Edit address
        [6] Edit phone number
        [7] Edit email address
        [0] Return to Profile Menu
        ====================""")
        user = input(f"Please select an option from the edit menu ({MIN_EDIT_MENU}-{MAX_EDIT_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_EDIT_MENU, MAX_EDIT_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the edit menu ({MIN_EDIT_MENU}-{MAX_EDIT_MENU})")
        else:
            if user == 1:
                first_name = create_first_name()
                if first_name == "cancel":
                    return
                else:
                    profile.first_name = first_name
            if user == 2:
                middle_name = create_middle_name()
                if middle_name == "cancel":
                    return
                else:
                    profile.middle_name = middle_name
            if user == 3:
                last_name = create_last_name()
                if last_name == "cancel":
                    return
                else:
                    profile.last_name = last_name
            if user == 4:
                street_address = create_street_address()
                if street_address == "cancel":
                    return
                city = create_city()
                if city == "cancel":
                    return
                province = create_province()
                if province == "cancel":
                    return
                postal_code = create_postal_code()
                if postal_code == "cancel":
                    return
                country = create_country()
                if country == "cancel":
                    return
                address = f"{street_address} {city} {province} {postal_code} {country}"
                profile.address = address
            if user == 5:
                birth_year = create_birth_year()
                if birth_year == "cancel":
                    return
                birth_month = create_birth_month()
                if birth_month == "cancel":
                    return
                if birth_month in [1, 3, 5, 7, 8, 10, 12]:
                    max_birth_day = 31
                elif birth_month in [4, 6, 9, 11]:
                    max_birth_day = 30
                elif birth_month == 2:
                    max_birth_day = 28
                birth_day = create_birth_day(max_birth_day)
                if birth_day == "cancel":
                    return
                date_of_birth = f"{birth_year}-{birth_month}-{birth_day}"
                profile.date_of_birth = date_of_birth
            if user == 6:
                phone_number = create_phone_number()
                if phone_number == "cancel":
                    return
                profile.phone_number = phone_number
            if user == 7:
                email_address = create_email_address()
                if email_address == "cancel":
                    return
                profile.email_address = email_address
            if user == 0:
                return


def profile_menu(profile):
    if profile.status == "ACTIVE":
        while True:
            print(f"""
            Banking System Prototype
            ====================
            Profile Menu
            --------------------
            Profile Number: {profile.profile_number}
            First Name: {profile.first_name}  Middle Name: {profile.middle_name}  Last Name: {profile.last_name}
            Date of Birth: {profile.date_of_birth}
            Address: {profile.address}
            Phone Number: {profile.phone_number}  Email Address: {profile.email_address}
            Status: {profile.status}
            --------------------""")
            for i in accounts_list:
                if i.profile_number == profile.profile_number:
                    i.display_details()
            print(f"""
            --------------------
            [1] Create Account
            [2] Select Account
            [3] Delete Account
            [4] Edit Profile
            [0] Return to Search Menu
            ====================""")
            user = input(f"Please select an option from the profile menu ({MIN_PROFILE_MENU_ACTIVE}-{MAX_PROFILE_MENU_ACTIVE}): ")
            try:
                user = int(user)
                if user not in range(MIN_PROFILE_MENU_ACTIVE, MAX_PROFILE_MENU_ACTIVE + 1):
                    raise ValueError
            except ValueError:
                print(
                    f"Invalid input, please select an option from the profile menu ({MIN_PROFILE_MENU_ACTIVE}-{MAX_PROFILE_MENU_ACTIVE})")
            else:
                if user == 1:
                    create_account(profile)
                elif user == 2:
                    user_search = input("Enter account number: ")
                    select_account(accounts_list, 0, len(accounts_list) - 1, user_search, profile)
                elif user == 3:
                    user_del = input("Enter account number: ")
                    delete_account(accounts_list, 0, len(accounts_list) - 1, user_del, profile)
                elif user == 4:
                    edit_profile(profile)
                if user == 0:
                    return
    else:
        while True:
            print(f"""
                   Banking System Prototype
                   ====================
                   Profile Menu
                   --------------------
                   Profile Number: {profile.profile_number}
                   First Name: {profile.first_name}  Middle Name: {profile.middle_name}  Last Name: {profile.last_name}
                   Date of Birth: {profile.date_of_birth}
                   Address: {profile.address}
                   Phone Number: {profile.phone_number}  Email Address: {profile.email_address}
                   Status: {profile.status}
                   --------------------""")
            for i in accounts_list:
                i.display_details()
            print(f"""
                   --------------------
                   [1] Reactivate Account
                   [0] Return to Search Menu
                   ====================""")
            user = input(f"Please select an option from the profile menu ({MIN_PROFILE_MENU_INACTIVE}-{MAX_PROFILE_MENU_INACTIVE}): ")
            try:
                user = int(user)
                if user not in range(MIN_PROFILE_MENU_INACTIVE, MAX_PROFILE_MENU_INACTIVE + 1):
                    raise ValueError
            except ValueError:
                print(
                    f"Invalid input, please select an option from the profile menu ({MIN_PROFILE_MENU_INACTIVE}-{MAX_PROFILE_MENU_INACTIVE})")
            else:
                if user == 1:
                    profile.status = "ACTIVE"
                    print("Profile reactivated")
                    return
                if user == 0:
                    return


def search_profile_by_profile_number(input_list, low, high, input_search):
    input_list.sort(key=lambda x: x.profile_number)
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].profile_number == input_search:
            profile_menu(input_list[mid])
        elif input_list[mid].profile_number > input_search:
            return search_profile_by_profile_number(input_list, low, mid - 1, input_search)
        else:
            return search_profile_by_profile_number(input_list, mid + 1, high, input_search)
    else:
        print("Profile not found")


def search_profile_by_phone_number(input_list, low, high, input_search):
    input_list.sort(key=lambda x: x.phone_number)
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].phone_number == input_search:
            profile_menu(input_list[mid])
        elif input_list[mid].phone_number > input_search:
            return search_profile_by_phone_number(input_list, low, mid - 1, input_search)
        else:
            return search_profile_by_phone_number(input_list, mid + 1, high, input_search)
    else:
        print("Profile not found")


def search_profile_by_email_address(input_list, low, high, input_search):
    input_list.sort(key=lambda x: x.email_address)
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].email_address == input_search:
            profile_menu(input_list[mid])
        elif input_list[mid].email_address > input_search:
            return search_profile_by_email_address(input_list, low, mid - 1, input_search)
        else:
            return search_profile_by_email_address(input_list, mid + 1, high, input_search)
    else:
        print("Profile not found")


def delete_profile(input_list, low, high, input_del):
    if len(input_list) == 0:
        print("No profile exists")
        return
    input_list.sort(key=lambda x: x.profile_number)
    if high >= low:
        mid = (high + low) // 2
        if input_list[mid].profile_number == input_del:
            input_list[mid].status = "INACTIVE"
            print("Profile deactivated successfully")
        elif input_list[mid].profile_number > input_del:
            return delete_profile(input_list, low, mid - 1, input_del)
        else:
            return delete_profile(input_list, mid + 1, high, input_del)
    else:
        print("Profile not found")


def display_menu():
    while True:
        print("""
        Banking System Prototype
        ====================
        Display Menu
        --------------------
        [1] By profile number
        [2] By last name
        [3] By date of birth
        [0] Return to Main Menu
        ====================""")
        user = input(f"Please select an option from the main menu({MIN_DISPLAY_MENU}-{MAX_DISPLAY_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_DISPLAY_MENU, MAX_DISPLAY_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the main menu({MIN_DISPLAY_MENU}-{MAX_DISPLAY_MENU})")
        else:
            if user == 1:
                display_profiles_by_profile_number(profiles_list)
            elif user == 2:
                display_profiles_by_last_name(profiles_list)
            elif user == 3:
                display_profiles_by_date_of_birth(profiles_list)
            elif user == 0:
                return


def search_menu():
    while True:
        print("""
        Banking System Prototype
        ====================
        Search Menu
        --------------------
        [1] By profile number
        [2] By phone number
        [3] By email address
        [0] Return to Main Menu
        ====================""")
        user = input(f"Please select an option from the search menu({MIN_SEARCH_MENU}-{MAX_SEARCH_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_SEARCH_MENU, MAX_SEARCH_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the search menu({MIN_SEARCH_MENU}-{MAX_SEARCH_MENU})")
        else:
            if user == 1:
                user_search = input("Enter profile number: ")
                search_profile_by_profile_number(profiles_list, 0, len(profiles_list) - 1, user_search)
            elif user == 2:
                user_search = input("Enter phone number: ")
                search_profile_by_phone_number(profiles_list, 0, len(profiles_list) - 1, user_search)
            elif user == 3:
                user_search = input("Enter email address: ")
                search_profile_by_email_address(profiles_list, 0, len(profiles_list) - 1, user_search)
            elif user == 0:
                return


def save_data(input_file, input_list):
    with open(input_file, "w") as file_data:
        for i in input_list:
            file_data.write(i.format_data())


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
        [0] Exit Program
        ====================""")
        user = input(f"Please select an option from the main menu({MIN_MAIN_MENU}-{MAX_MAIN_MENU}): ")
        try:
            user = int(user)
            if user not in range(MIN_MAIN_MENU, MAX_MAIN_MENU + 1):
                raise ValueError
        except ValueError:
            print(f"Invalid input, please select an option from the main menu({MIN_MAIN_MENU}-{MAX_MAIN_MENU})")
        else:
            if user == 1:
                create_profile()
            elif user == 2:
                display_menu()
            elif user == 3:
                search_menu()
            elif user == 4:
                user_del = input("Enter profile number: ")
                delete_profile(profiles_list, 0, len(profiles_list) - 1, user_del)
            elif user == 0:
                print("Saving data.")
                save_data("profiles.csv", profiles_list)
                save_data("accounts.csv", accounts_list)
                print("Ending program.")
                return 0


def main():
    main_menu()


if __name__ == "__main__":
    main()
