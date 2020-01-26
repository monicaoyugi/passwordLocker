#!/usr/bin/env python3

from user_credentials import Credentials,User

def create_user(fname, lname, password):
    '''
    Function that creates a new user account.
    '''
    new_user = User(fname, lname, password)
    return new_user


def save_user(user):
    '''
    Function that saves a new user.
    '''
    User.save_user(user)


def verify_user(first_name, password):
    '''
    Function that verifies if user exists.
    '''
    checking_user = User.check_user(first_name, password)
    return checking_user


def generate_password(self):
    '''
    Fucntioin that generates password.
    '''
    gen_password = Credentials.generate_password(self)
    return gen_password

def create_credential(user_name, site_name, account_name, password):
    '''
    Function that creates new credentials.
    '''
    new_credential = Credentials(user_name, site_name, account_name, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential.
    '''
    Credentials.save_credential(credential)


def display_credentials(username):
    '''
    Fucntion to display credentials saved.
    '''
    return Credentials.display_credential(username)
def copy_credential(site_name):
    '''
    Function that copies credentials details to the clipborad.
    '''
    return Credentials.copy_credential(site_name)


def find_by_site(site_name):
    '''
    Function that searches for a site name.
    '''
    return Credentials.find_by_site_name(site_name)

def delete_credential(credential):
    '''
    Function that deletes credentials by site name.
    '''
    credential.del_credential()

def check_existing_credentials(site_name):
    '''
    Function that checks if a credential exists.
    '''
    return Credentials.credential_exist(site_name)


