import unittest # Importing the unittest module allows us to test
from user_data import Users # Importing the users class from user_data module
import pyperclip # importing pyperclip for copy and past function.

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the users class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user_data = Users ("Instagram","@levim","levi@email.com","axolotl") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user_data.account_name,"Instagram")
        self.assertEqual(self.new_user_data.username,"@levim")
        self.assertEqual(self.new_user_data.email,"levi@email.com")
        self.assertEqual(self.new_user_data.password,"axolotl")

    def test_save_user_data(self):
        '''
        test_save_user_data test case to test if the users object is saved into
         the account details.
        '''
        self.new_user_data.save_account() # saving the new account details
        self.assertEqual(len(Users.account_details),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Users.account_details = []

    def test_save_multiple_accounts(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user_data.save_account()
            test_account = Users("account","username","test@user.com","password") #regestering a new account
            test_account.save_account()
            self.assertEqual(len(Users.account_details),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a saved account from our account details list
            '''
            self.new_user_data.save_account()
            test_account = Users("account","username","test@user.com","password") # registered new account
            test_account.save_account()

            self.new_user_data.delete_account()
            self.assertEqual(len(Users.account_details),1)

    def test_find_details_by_username(self):
        '''
        test to check if we can find the details of an account by typing the username and display information
        '''

        self.new_user_data.save_account()
        test_account = Users("account","username","test@user.com","password") #registered new account
        test_account.save_account()

        found_account = Users.find_by_username("username")

        self.assertEqual(found_account.email,test_account.email)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account details.
        '''

        self.new_user_data.save_account()
        test_account = Users("account","username","test@user.com","password") #registered new account
        test_account.save_account()

        account_exists = Users.account_exist("username")

        self.assertTrue(account_exists)

    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Users.display_accounts(),Users.account_details)

    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from a found account details
        '''

        self.new_user_data.save_account()
        Users.copy_password("password")

        self.assertEqual(self.new_user_data.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()