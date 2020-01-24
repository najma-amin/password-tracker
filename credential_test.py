import unittest
from Credential import User, Credential
import pyperclip



class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        this is setup method to run before each testcase
        '''
        self.new_user = User("najma", "1234abcd")
        
    def tearDown(self):
        User.user_list = []
        
    def test__init__(self):
        '''
        method to test if object is well initialized 
        '''
        self.assertEqual(self.new_user.lastname,"najma")
        self.assertEqual(self.new_user.password,"1234abcd")
    
    def test_save_user(self):
        '''
        method to test if the user object is saved into the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),0)
        
        class TestCredential(unittest.TestCase):
        '''
    Test class that defines teself.3+st cases for the credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def test_confirm_login(self):
        '''
        Method to test login functionality.
        '''
        self.new_user = User('najma','12345abcd')
        self.new_user.save_user()
        user2 = User('najma', '123abcd')
        user2.save_user()
        for user in User.user_list:
            if user.lastname == user2.lastname and user.password == user2.password:
                current_user = user.lastname
        return current_user
        self.assertEqual(current_user, Credential.confirm_login(user2.password, user2.lastname))