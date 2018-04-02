#!/usr/bin/env python3.6
from user_data import Users


def create_account(account_name,username,email,password):
    '''
    Function to create account detail
    '''
    new_account = Users(account_name,username,email,password)
    return new_account


def save_account(user_data):
    '''
    Function to the account details
    '''
    user_data.save_account()

def del_account(user_data):
    '''
    Function to delete account details
    '''
    user_data.delete_account()

def find_account(username):
    '''
    Function that finds account details using the username
    '''
    return Users.find_by_username(username)

def check_existing_accounts(username):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Users.account_exist(username)

def display_accounts():
    '''
    Function that returns all the saved contacts
    '''
    return Users.display_accounts()





def main():
    print("Hello Welcome to your Password Locker. Enter your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, ex -exit the account details ")

                    short_code = input().lower()

                    if short_code == 'ca':
                            print("New Account:")
                            print("-"*10)

                            print ("Name of Online Platform: ....")
                            account_name = input()

                            print("username used: ...")
                            username = input()

                            print("Email address used: ...")
                            email = input()

                            print("Password used: ...")
                            password = input()


                            save_account(create_account(account_name,username,email,password)) # create and save new account details.
                            print ('\n')
                            print(f"New account {account_name} {username} created and saved")
                            print ('\n')

                    elif short_code == 'da':

                            if display_accounts():
                                    print("Here is a list of your online platforms")
                                    print('\n')

                                    for user_data in display_accounts():
                                            print(f"{user_data.account_name} {user_data.username} .....{user_data.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved")
                                    print('\n')

                    elif short_code == 'fa':

                            print("Enter the username you want to search for")

                            search_username = input()
                            if check_existing_accounts(search_username):
                                    search_account = find_account(search_username)
                                    print(f"{search_account.account_name} {search_account.username}")
                                    print('-' * 20)

                                    print(f"User name.......{search_account.username}")
                                    print(f"online platform.......{search_account.account_name}")
                                    print(f"Password.......{search_account.password}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()