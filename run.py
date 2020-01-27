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


def main():
    print('\n')

    print("")
    print("Hello there! Welcome to Password Locker.")
    while True:
        print("*"*60)
        print('\n')
        print("Use these codes to navigate: \n ca - Create an account \n li - Log in \n ex - Exit")
        print('\n')
        short_code = input("Enter a choice: ").lower().strip()

        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print('\n')
            print("-"*60)
            print('\n')
            print("To create a new account:")
            first_name = input('Enter your first name - ').strip()
            last_name = input('Enter your last name - ').strip()
            password = input('Enter password - ').strip()
            save_user(create_user(first_name, last_name, password))
            print('\n')
            print(f"New account created for {first_name} {last_name} using password {password}")
        
        elif short_code == 'li':
            print("-"*60)
            print('\n')
            print("Enter your account details to log in.")
            user_name = input("Enter your first name - ").strip()
            password = str(input("Enter your password - "))
            user_exists = verify_user(user_name, password)
            if user_exists == user_name:
                print('\n')
                print(f"Welcome {user_name}. Please choose an option to continue.")
                while True:
                    print("-"*60)
                    print("Navigation codes: \n cc - To create a credential \n dc - To display all credentials \n fc - To find a credential \n cp - To copy password \n del - To delete a credential \n ex - Exit")
                    print('\n')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'ex':
                        print('\n')
                        print(f"Goodbye {user_name}")
                        break
                    elif short_code == 'cc':
                        print('\n')
                        print("Enter your credential details:")
                        site_name = input("Enter the site's name - ").strip()
                        account_name = input("Enter your account's username - ").strip()

                        while True:
                            print('\n')
                            print("-"*60)
                            print("Choose the password method you would like. Use keys: \n ep - To enter a password \n gp - To generate a password \n ex - Exit")
                            password_choice = input("Enter an option: ").lower().strip()
                            print("-"*60)
                            if password_choice == 'ep':
                                print('\n')
                                password = input("Enter your password: ").strip()
                                break
                            elif password_choice == 'gp':
                                password = generate_password(password)
                                break
                            elif password_choice == 'ex':
                                break
                            else:
                                print("Bummer! You entered the wrong option. Please try again.")
                        save_credential(create_credential(user_name, site_name, account_name,password))
                        print('\n')
                        print(f"Credential created: \n Site name: {site_name} - Account Username: {account_name} - Password: {password}")

                    elif short_code == 'dc':
                        print('\n')

                        if display_credentials(user_name):
                            print("Here is a list of all your creddentials:")
                            print('\n')
                            for credential in display_credentials(user_name):
                                print(f"Site name: {credential.site_name} - Account name: {credential.account_name} - Password: {credential.password}")
                        else:
                            print('\n')
                            print("You don't seem to have any credential saved yet.")
                            print('\n')


                    elif short_code == 'fc':
                        search_site = input("Enter the site name you are searching for: \n")
                        if check_existing_credentials(search_site):
                            result = find_by_site(search_site)
                            print(f"Search result: Site name: {result.site_name} - Account name: {result.account_name} - Password: {result.password}")
                        else:
                            print("No such credential exists. Please try again!")
                    
                    elif short_code == 'cp':
                        print('\n')
                        chosen_site = input("Enter the site name for the credential you want to copy: ")
                        copy_credential(chosen_site)
                        print('\n')
                    elif short_code == 'del':
                        print('\n')
                        print("Enter the name of the site credential you want to delete.")
                        print('\n')
                        answer = input("Enter choice: ")

                        if check_existing_credentials(answer):
                            answer = find_by_site(answer)
                            delete_credential(answer)
                            print("Credentials successfully deleted!")

                        else:
                            ("No such credential exists!")
                        
                    else:
                        print("Bummer! You entered the wrong option. Please try again.")
                
                else:
                    print('\n')
                    print("Bummer! You entered the wrong details Please try again or create an account.")

            else:
                print("-"*60)
                print('\n')
                print("I really didn't get that. Please use the short codes.")


if __name__ == '__main__':
    main()