#!/usr/bin/env python3.6
from user_data import Users


def create_contact(account_name,username,email,password):
    '''
    Function to create account detail
    '''
    new_account = Users(account_name,username,email,password)
    return new_account


