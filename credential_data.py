class Credential:
    """
    Class that generates new instances of credential
    Generate password for the user hold the username and the password...
    """

    pass

    account_desc = [] #this is where the passwords will be held once generated

    def __init__(self,gen_passcode,): #the intance variable

         
            self.gen_passcode = gen_passcode


    account_desc = [] # Empty container for storing passwords
     # Init method up here

    def store_password(self):

        '''
        store_password method helps store the generated passwords for the users
        '''

        Credential.account_desc.append(self)  