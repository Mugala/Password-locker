class Users:
    """
    Class that generates new instances of users. This class will hold the users data that they input,
    the online platform email address their username and date created.
    """

    pass

    account_details = [] #This is where we will store all the accounts and their details

    def __init__(self,account_name,username,email,password): #the intance variables that will represent the users details for different accounts

         
            self.account_name = account_name
            self.username = username
            self.email = email
            self.password = password


    account_details = [] # Empty container no account registered
     # Init method up here
    def save_account(self):

        '''
        save_account method saves users objects into account_details
        '''

        Users.account_details.append(self)   

    def delete_account(self):

        '''
        delete_account method deletes a saved account details from the account_details
        '''

        Users.account_details.remove(self) 

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns the account details that matches that username.

        Args:
            username: Usernme that matches the account
        Returns :
            Account details of the user that matches the username.
        '''

        for user_data in cls.account_details:
            if user_data.username == username:
                return user_data