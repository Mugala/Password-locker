#!/usr/bin/env python3.6
from user_data import Users


def create_contact(account_name,username,email,password):
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