import unittest
import user_credentials_test, user_credentials_test

class TestUser(unittest.TestCase);
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    
    
    def setUp(self):
        '''
        Set up method to run before each check if pyperclip is installedtest cases.
        '''
        self.new_user = User('Monica', 'Oyugi', 'ndito123')  #create user object
    
    def test__init__(self):
        '''
        Test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.first_name, "Monica")
        self.assertEqual(self.new_user.last_name, "Oyugi")
        self.assertEqual(self.new_user.password, "ndito123")

        