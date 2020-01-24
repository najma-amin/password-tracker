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
        