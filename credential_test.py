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
        
    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential('twitter','najma','12345abcd')
        
    def test__init__(self):
        '''
        test__init__ test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name,'twitter')
        self.assertEqual(self.new_credential.username,'najma')
        self.assertEqual(self.new_credential.password,'12345abcd')
        
    def test_save_credential(self):
        '''
        Test to confirm if the new credential is saved to the credentials list
        '''
        self.new_credential.save_credential()
        instagram = Credential('Instagram','najma','12345abcd')
        instagram.save_credential()
        self.assertEqual(len(Credential.credential_list),9)
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.Czredential_list = []
        User.user_list = []
        
    def test_display_credential(self):
        '''
        Test to check if credentials display method displays
        '''
        self.new_credential.save_credential()
        instagram = Credential('Instagram','najma','1234abcd')
        instagram.save_credential()
        facebook = Credential('Facebook','najma','1234abcd')
        facebook.save_credential()
        self.assertEqual(len(Credential.display_credential(instagram.username)), 9)
        
    def test_find_by_account_name(self):
        '''
        Test method for finding a credential site_name
        '''
        self.new_credential.save_credential()
        instagram = Credential('Instagram','najma','1234abcd')
        instagram.save_credential()
        credential_exist = Credential.find_by_account_name('Instagram')
        # self.assertEqual(credential_exists, instagram)
        
        
    def test_copy_credential(self):
        '''
        Test method for copy credential functionality
        '''
        self.new_credential.save_credential()
        instagram = Credential('Instagram','najma','12345abcd')
        instagram.save_credential()
        find_credential = None
        for credential in Credential.user_credential_list:
            find_credential =Credential.find_by_account_name(credential.account_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.account_name)
        self.assertEqual('12345abcd',pyperclip.paste())
        print(pyperclip.paste())
        
        
if __name__ == "__main__":
    unittest.main()



