import unittest
import user_credentials_test, user_credentials_test
import pyperclip

class TestUser(unittest.TestCase):
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

    def tearDown(self):
        '''
        A method that clears the users list after every test.
        '''
        User.users_list = []


    def test_save_user(self):
        '''
        Test case to test if the user object is saved to the users list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)


    
    def test_check_user(self):
        '''
        Test case to test whether login feature is functional.
        '''
        self.new_user = User('Monica', 'Oyugi', 'ndito123')
        self.new_user.save_user()
        user2 = User('Martin', 'Owiti', '@#Omosh')
        user2.save_user()

    for user in User.users_list:
        if user.first_name == user2.first_name and user.password == user2.password:
            current_user = user.first_name
    return current_user
    
    self.assertEqual(current_user, User.check_user(user2,password, user2.first_name))

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = credentials ("Monica","nyaroyugi","Adhis@000")

    def test__init__(self):
        '''
        Test case to check if creation of credential instances is properly done.
        '''
        self.assertEqual(self.new_credential.user_name, "Monica")
        self.assertEqual(self.new_credential.site_name, "Twitter")
        self.assertEqual(self.new_credential.account_name, "nyaroyugi")
        self.assertEqual(self.new_credential.password, "Adhis@000")

