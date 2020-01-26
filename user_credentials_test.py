import unittest
import user_credentials_test, user_credentials_test
import pyperclip
from user_credentials import Credentials
from user_credentials import User

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
        self.new_credential = Credentials("Monica","Twitter","nyaroyugi","Adhis@000")

    def test__init__(self):
        '''
        Test case to check if creation of credential instances is properly done.
        '''
        self.assertEqual(self.new_credential.user_name, "Monica")
        self.assertEqual(self.new_credential.site_name, "Twitter")
        self.assertEqual(self.new_credential.account_name, "nyaroyugi")
        self.assertEqual(self.new_credential.password, "Adhis@000")
    
    def tearDown(self):
        '''
        A method that clears the users credentials list after every test.
        '''
        Credentials.credentials_list = []


    def test_save_credentials(self):
        '''
        Test case to check if we can save credentials to the credentials list.
        '''
        self.new_credential.save_credential()
        facebook = Credentials("Kev", "Facebook", "Kibugi", "Word123")
        facebook.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)


    def test_display_credentials(self):
        '''
        Test case to test if our objects show.
        '''
        self.new_credential.save_credential()
        facebook = Credentials("Kev", "Facebook", "Kibugi", "word123")
        facebook.save_credential()
        gmail = Credentials('Joy','Gmail','Ondiba','sheba456')
        gmail.save_credential()
        self.assertEqual(len(Credentials.display_credential(facebook.user_name)), 1)


    def test_find_by_site_name(self):
        '''
        Test case to test if we can search credential by site_name and return the correct credential.
        '''
        self.new_credential.save_credential()
        gmail = Credentials('Joy','Gmail','Ondiba','sheba456')
        gmail.save_credential()
        credential_exists = Credentials.find_by_site_name('Gmail')
        self.assertEqual(credential_exists, gmail)


    def test_copy_credential(self):
        '''
        Test case to test if the copy credential function copies the correct credential.
        '''
        self.new_credential.save_credential()
        twitter = Credentials('Monica','Twitter','nyaroyugi','Adhis@000')
        twitter.save_credential()
        find_credential = None
        for credential in Credentials.users_credentials_list:
            find_credential = Credentials.find_by_site_name(credential.site_name)
            pyperclip.copy(find_credential.password)
        Credentials.copy_credential(self.new_credential.site_name)
        self.assertEqual('Adhis@000', pyperclip.paste())

    
    def test_delete_credential(self):
        '''
        Test case to test if we can delete a saved credential.
        '''
        self.new_credential.save_credential()
        new_credential = Credentials('Joy','Gmail','Ondiba','sheba456')
        new_credential.save_credential()

        self.new_credential.del_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)


    def test_credential_exists(self):
        '''
        Test case to check if a credential exists in the credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('Joy','Gmail','Ondiba','sheba456')
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("Gmail")
        self.assertTrue(credential_exists)



if __name__ == '__main__':
    unittest.main()

