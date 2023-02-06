class TestValidInput:
    ''' This class used to implement chain of input validation in
        stage by stage manner.
    '''

    def __init__ ( self ) -> None:

        # show this text to user to inform what to input.
        self.inputText = None

        # list to store all validation function for this input
        self.validationFunctionList = []

        # list to store all error message to inform user why some validation not pass
        self.errorMessageList = []

    def addInputText( self, inputText ):
        ''' add input text of this test object.
        '''
        self.inputText = inputText

    def addValidationFunction( self, validationFunction ):
        ''' add validation function to list of validation function to use with this input.
            validation function should return True if pass else, return False.      
        '''
        self.validationFunction.append( validationFunction )

    def executeAllValidation( self ):
        ''' execute all validation function to verify this input text from user.
        '''
        # get input from user.
        userInput = input( self.inputText )
        
        #loop get all validation function
        for validationFunction in range( len ( self.validationFunctionList ) ):
            thisValidationFunction = self.validationFunctionList[ validationFunction ]

            # validate input according to each function
            thisFunctionResult = thisValidationFunction( userInput )

            # if input is valid
            if thisFunctionResult:

            # perform another function

            # if input is invalid

            # ask user to input again and check all validation function again.



























