
#!/usr/bin/env python3.6
from Credential import User,Credential

def create_user(lastname,password):
    '''
    Function to create a new user
    '''
    new_user = User(lastname, password)
    return new_user
def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def authenticate_user(lastname, password):
    '''
    Function to authenticate a user
    '''
    authenticated_user = Credential.confirm_login(lastname, password)
    return authenticated_user
def create_credential(account_name,username,password):
    '''
    Function to create a new credential object
    '''
    new_credential = Credential(account_name,username,password)
    return new_credential
def save_credential(credential):
    '''
    Function to save a created credential
    '''
    Credential.save_credential(credential)
def generate_password():
    '''
    Function to randomly generate password
    '''
    password_generate = Credential.generate_password
    return password_generate
def display_credential(username):
    '''
    Function to display credentials
    '''
    return Credential.display_credential(username)
def copy_credential(account_name):
    '''
    Function to copy a credential to the clipboard
    '''
    return Credential.copy_credential(account_name)

def main():
   print(' ')
   print('Welcome to Password Locker.')
   while True:
       print(' ')
       print("-"*40)
       print('Use these short codes: cr-Create Password-Locker account,  log-Login, ex-Exit')
       short_code = input('Enter short code here: ').lower().strip()
       if short_code == 'ex':
           break
       elif short_code == 'cr':
           print("-"*40)
           print(' ')
           print('To create a new account:')
           lastname = input('Choose a lastname - ').strip()
           password = input('Choose a password - ').strip()
           save_user(create_user(lastname,password))
           print(" ")
           print(f'Your Password-Locker account lastname is : {lastname}  and password is: {(password)}')

       elif short_code == 'log':
           print("-"*40)
           print(' ')
           print('To login:')
           lastname = input('Enter your Password-Locker username - ').strip()
           password = str(input('Enter your password - '))
           user_authenticated = authenticate_user(lastname,password)
           if user_authenticated == lastname:
               print(" ")
               print(f'Welcome {lastname}. You have successfully logged in. Choose short code to continue')
               print(' ')
               while True:
                   print("-"*40)
                   print('Your credentials short codes: c-Create credential, d-Display Credentials, p-Copy Password, ex-Exit')
                   short_code = input('Enter short code: ').lower().strip()
                   print("-"*40)
                   if short_code == 'ex':
                       print(" ")
                       print(f'Goodbye {lastname}')
                       break
                   elif short_code == 'c':
                       print(' ')
                       print('Enter your credential account information:')
                       account_name = input('Enter the account name - ').strip()
                       username = input('Enter your username - ').strip()
                       password = input('Enter your password - ').strip()

                       while True:
                           print(' ')
                           print("-"*40)
                           print('Select option for entering a password:  e-Enter your own password, g-Generate a password ,ex-Exit')
                           passwrd_select = input('Enter an option: ').lower().strip()
                           print("-"*40)
                           if passwrd_select == 'e':
                               print(" ")
                               password = input('Enter your password: ').strip()
                               break
                           elif passwrd_select == 'g':
                               password = generate_password()
                               break
                           elif passwrd_select == 'ex':
                               break
                           else:
                               print('Incorrect entry. Try again.')
                       save_credential(create_credential(account_name,username,password))
                       print(' ')
                       print(f'Credential Created: Account Name: {account_name} - User name: {username} - Password: {password}')
                       print(' ')
                   elif short_code == 'd':
                       print(' ')
                       if display_credential(username):
                           print('Your credential account list:')
                           print(' ')
                           for credential in display_credential(username):
                               print(f'Account Name: {credential.account_name}-User Name: {credential.username}-Password: {credential.password}')
                           print(' ')
                       else:
                           print(' ')
                           print("No credential saved")
                           print(' ')
                   elif short_code == 'p':
                       print(' ')
                       chosen_account_name = input('Enter the account name for the credential password to copy: ')
                       copy_credential(chosen_account_name)
                       print('')
                       print('Paste copied account_name password here:')
                       
                   else:
                       print('Incorrect entry.Try again.')
           else:
               print(' ')
               print('Incorrect entry. Try again or Create an Account.')        
       else:
           print("-"*40)
           print(' ')
           print('Incorrect entry. Try again.')
                
if __name__ == "__main__":
   main()
