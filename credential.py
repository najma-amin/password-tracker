import random 
import string
import  pyperclip

class User:
    '''
    class that will generate new instances of users.
    '''
    user_list = []
    def __init__(self,lastname ,password):
        
        '''
        init method that gives the blueprint of the object instantiated
        '''
        self.lastname = lastname
        self.password = password
        
    def save_user (self):
        '''
        amethod  to save uset object to user_list
        '''
        User.user_list.append(self)