import unittest # Importing the unittest module allows us to test
from credential_data import Credential # Importing the users class from user_data module


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
        self.new_credential_data = Credential ("axolotl") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential_data.passcode,"axolotl")
