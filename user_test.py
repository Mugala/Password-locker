import unittest # Importing the unittest module allows us to test
from user_data import Users # Importing the users class from user_data module

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


if __name__ == '__main__':
    unittest.main()